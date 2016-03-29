#!/bin/sh

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

WLST=$ORACLE_HOME/oracle_common/common/bin/wlst.sh

cd build/

echo ''
echo '   ##########################################################   '
echo '   ------------------   Building project   ------------------   '
echo '   ##########################################################   '
echo ''
bash ./buildForCluster.sh

echo ''
echo '   ##########################################################   '
echo '   -----------------   Performing cleanup   -----------------   '
echo '   ##########################################################   '
echo ''
rm -r $DOMAIN_HOME/$DOMAIN_NAME

echo ''
echo '   ##########################################################   '
echo '   ------------------   Creating domain   -------------------   '
echo '   ##########################################################   '
echo ''
$WLST create-domain.py

echo ''
echo '   ##########################################################   '
echo '   --------------   Starting WebLogic server   --------------   '
echo '   ##########################################################   '
echo ''
$WLST start-domain.py

echo ''
echo '   ##########################################################   '
echo '   -----------------   Creating cluster   -------------------   '
echo '   ##########################################################   '
echo ''
$WLST create-cluster.py

echo ''
echo '   ##########################################################   '
echo '   -Please manually start up managed servers for the cluster-   '
echo '   ##########################################################   '
echo ''

cd ..