#!/bin/sh
# Use -w | --wait flag to pause between setup and execution

# Read arguments
while :; do
    case $1 in
        -w|--wait)
        WAIT="true"
        break
        ;;
    esac

    shift
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
rm -r $DOMAIN_HOME/applications

echo ''
echo '   ##########################################################   '
echo '   ------------------   Creating domain   -------------------   '
echo '   ##########################################################   '
echo ''
$WLST create-domain-otd.py

echo ''
echo '   ##########################################################   '
echo '   --------------   Starting WebLogic server   --------------   '
echo '   ##########################################################   '
echo ''
$WLST start-domain-otd.py

echo ''
echo '   ##########################################################   '
echo '   -----------------   Creating cluster   -------------------   '
echo '   ##########################################################   '
echo ''
$WLST create-cluster-otd.py

echo ''
echo '   ##########################################################   '
echo '   -----------------   Starting cluster   -------------------   '
echo '   ##########################################################   '
echo ''
$WLST start-cluster-otd.py

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
$WLST deployWithClusterAndOTD.py

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
echo '   --------------   Stopping WebLogic server   --------------   '
echo '   ##########################################################   '
echo ''
$WLST stop-clustered-domain-otd.py

cd ..