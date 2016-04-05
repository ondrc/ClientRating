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

function pause() {
    read -p "$*"
}

ORACLE_HOME="${ORACLE_HOME:=/opt/wls/Oracle_Home}"
WL_HOME="${WL_HOME:=$ORACLE_HOME/wlserver}"
DOMAIN_HOME="${DOMAIN_HOME:=/opt/wls}"
DOMAIN_NAME="${DOMAIN_NAME:=domain}"

echo ''
echo '   ##########################################################   '
echo '   ----------- Running with following environment------------   '
echo '   ##########################################################   '
echo ''
echo ''
echo 'ORACLE_HOME='$ORACLE_HOME
echo 'WL_HOME='$WL_HOME
echo 'DOMAIN_HOME='$DOMAIN_HOME
echo 'DOMAIN_NAME='$DOMAIN_NAME
echo ''

if [ -n "$WAIT" ];
then
    echo 'Will wait for confirmation after setup'
    echo ''
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
rm -r $DOMAIN_HOME/$DOMAIN_NAME
rm -r $DOMAIN_HOME/prod/$DOMAIN_NAME

echo ''
echo '   ##########################################################   '
echo '   ----------------   Creating test domain   ----------------   '
echo '   ##########################################################   '
echo ''
$WLST create-domain.py

echo ''
echo '   ##########################################################   '
echo '   -------------   Creating production domain   -------------   '
echo '   ##########################################################   '
echo ''
$WLST create-prod-domain.py

echo ''
echo '   ##########################################################   '
echo '   --------------   Starting WebLogic server   --------------   '
echo '   ##########################################################   '
echo ''
$WLST start-domains-t2p.py

echo ''
echo '   ##########################################################   '
echo '   ----------------   Creating partitions   -----------------   '
echo '   ##########################################################   '
echo ''
$WLST create-partitions.py

echo ''
echo '   ##########################################################   '
echo '   ----------   Creating production partitions   ------------   '
echo '   ##########################################################   '
echo ''
$WLST create-prod-partitions.py

echo ''
echo '   ##########################################################   '
echo '   ---------------   Creating data sources   ----------------   '
echo '   ##########################################################   '
echo ''
$WLST create-datasources.py

echo ''
echo '   ##########################################################   '
echo '   ----------   Creating production data sources   ----------   '
echo '   ##########################################################   '
echo ''
$WLST create-prod-datasources.py

echo ''
echo '   ##########################################################   '
echo '   ----------------  Deploying application   ----------------   '
echo '   ##########################################################   '
echo ''
$WLST deploy.py

echo ''
echo '   ##########################################################   '
echo '   ---------  Deploying application to production   ---------   '
echo '   ##########################################################   '
echo ''
$WLST deploy-prod.py

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
echo '   ----------------  Sending prod request   -----------------   '
echo '   ##########################################################   '
echo ''
curl http://localhost:8001/customer-service/CustomerService-1.0-SNAPSHOT/resources/customers

echo ''
echo '   ##########################################################   '
echo '   --------------  Transferring to production   -------------   '
echo '   ##########################################################   '
echo ''
$WLST transfer-partitions.py

if [ -n "$WAIT" ]
then
    pause 'Press [ENTER] to continue'
fi

echo ''
echo '   ##########################################################   '
echo '   ----------------  Sending prod request   -----------------   '
echo '   ##########################################################   '
echo ''
curl http://localhost:8001/customer-service/CustomerService-1.0-SNAPSHOT/resources/customers

echo ''
echo '   ##########################################################   '
echo '   ------------------   Stopping domains  -------------------   '
echo '   ##########################################################   '
echo ''
$WLST stop-domains-t2p.py

cd ..