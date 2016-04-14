#!/bin/sh
# Use -w | --wait flag to pause between setup and execution

# Read arguments
for key in "$@"
do
    case $key in
        -w|--wait)
        WAIT="true"
        ;;
    esac
done

# Pause until [ENTER] is pressed
#   $1 The text to display while waiting
function pause() {
    read -p "$*"
}

# Check if WebLogic server is listening
#   $1 Server port to search for
wls_is_listening() {
  CHECK=$(curl -I localhost:${1} 2>/dev/null | head -n 1 | cut -d$' ' -f2)
  if [ -z "$CHECK" ]; then
    return 1
  else
    return 0
  fi
}

# Wait for host:port to become active
#   $1 Port to check
#   $2 Waiting timeout in seconds
wait_for_weblogic() {
  START_TIME=`date +%s`
  TIMEOUT='false'
  while [ "${TIMEOUT}" = 'false' ] && ! wls_is_listening "${1}"; do
    PASSED_TIME=$((`date +%s` - ${START_TIME}))
    if [ "${PASSED_TIME}" -gt "${2}" ]; then
      echo 'Port check timeout after '${PASSED_TIME}' seconds'
      TIMEOUT='true'
    else
      if [ "$((PASSED_TIME%10))" -eq '0' ]; then
        printf "${PASSED_TIME}"
      else
        printf '.'
      fi
      sleep 1;
    fi
  done
  if [ "${TIMEOUT}" = 'false' ]; then
    return 0
  else
    return 1
  fi
}

ORACLE_HOME="${ORACLE_HOME:=/opt/wls/Oracle_Home}"
WL_HOME="${WL_HOME:=$ORACLE_HOME/wlserver}"

echo ''
echo '   ##########################################################   '
echo '   ----------- Running with following environment------------   '
echo '   ##########################################################   '
echo ''
echo ''
echo 'ORACLE_HOME='$ORACLE_HOME
echo 'WL_HOME='$WL_HOME
echo 'PROXY_URL='$PROXY_URL
echo 'JDK_ARCHIVE='$JDK_ARCHIVE
echo 'WLS_ARCHIVE='$WLS_ARCHIVE
echo 'DOCKER_VM='$DOCKER_VM
echo ''

if [ -z "$JDK_ARCHIVE" ];
then
    echo 'Please provide JDK_ARCHIVE property with full path to a JDK install archive for Linux x64'
    exit
fi

if [ -z "$WLS_ARCHIVE" ];
then
    echo 'Please provide WLS_ARCHIVE property with full path to a WebLogic installation jar'
    exit
fi

if [ -n "$WAIT" ];
then
    echo 'Will wait for confirmation after setup'
fi

WLST=$ORACLE_HOME/oracle_common/common/bin/wlst.sh

cd build/

echo ''
echo '   ##########################################################   '
echo '   ------------------   Building project   ------------------   '
echo '   ##########################################################   '
echo ''
bash ./build.sh

echo ''
echo '   ##########################################################   '
echo '   -----------------   Performing cleanup   -----------------   '
echo '   ##########################################################   '
echo ''
docker rm AdminServer
docker rmi weblogic

echo ''
echo '   ##########################################################   '
echo '   ----------------   Building docker image   ---------------   '
echo '   ##########################################################   '
echo ''
mkdir -p /tmp/docker
cp $JDK_ARCHIVE /tmp/docker
cp $WLS_ARCHIVE /tmp/docker
cp docker/Dockerfile /tmp/docker
cp create-domain.py /tmp/docker
docker build \
    -f /tmp/docker/Dockerfile \
    --build-arg JDK_ARCHIVE=$(basename $JDK_ARCHIVE) \
    --build-arg WLS_ARCHIVE=$(basename $WLS_ARCHIVE) \
    --build-arg PROXY_URL=$PROXY_URL \
    -t weblogic \
    /tmp/docker
rm -r /tmp/docker

if [ -n "$DOCKER_VM" ];
then
    echo ''
    echo '   ##########################################################   '
    echo '   ----------------   Creating port forward   ---------------   '
    echo '   ##########################################################   '
    echo ''
    VBoxManage controlvm $DOCKER_VM natpf1 "admin,tcp,127.0.0.1,7001,,7001"
    echo 'Created port forward from docker VM '$DOCKER_VM' port 7001 to local port 7001'
fi

echo ''
echo '   ##########################################################   '
echo '   ----------------   Starting docker image   ---------------   '
echo '   ##########################################################   '
echo ''
docker run -d \
    -p 7001:7001 \
    --name AdminServer \
    weblogic

wait_for_weblogic 7001 300
echo ''

echo ''
echo '   ##########################################################   '
echo '   ----------------   Creating partitions   -----------------   '
echo '   ##########################################################   '
echo ''
$WLST create-partitions.py

echo ''
echo '   ##########################################################   '
echo '   ----------------   Creating data source   ----------------   '
echo '   ##########################################################   '
echo ''
$WLST create-datasources.py

echo ''
echo '   ##########################################################   '
echo '   ----------------  Deploying application   ----------------   '
echo '   ##########################################################   '
echo ''
$WLST deployToDocker.py

if [ -n "$WAIT" ]
then
    pause 'Press [ENTER] to continue'
fi

echo ''
echo '   ##########################################################   '
echo '   ----------------  Sending test request   -----------------   '
echo '   ##########################################################   '
echo ''
curl http://localhost:7001/customer-service/CustomerService-1.0-SNAPSHOT/resources/customers

echo ''
echo '   ##########################################################   '
echo '   ---------------   Stopping docker image   ----------------   '
echo '   ##########################################################   '
echo ''
docker stop AdminServer

if [ -n "$DOCKER_VM" ];
then
    echo ''
    echo '   ##########################################################   '
    echo '   ----------------   Removing port forward   ---------------   '
    echo '   ##########################################################   '
    echo ''
    VBoxManage controlvm $DOCKER_VM natpf1 delete "admin"
    echo 'Removed port forward from docker VM '$DOCKER_VM' port 7001 to local port 7001'
    echo ''
fi

cd ..