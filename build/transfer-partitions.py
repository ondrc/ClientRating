domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")


# Export test domain partitions
connect('weblogic', 'welcome1', 't3://localhost:7001')

status = exportPartition('Partition-0', domain_home)
System.out.print('Exporting Partition-0')
while(status.getState()<2): Thread.sleep(100); System.out.print('.')
print('')

status = exportPartition('Partition-1', domain_home)
System.out.print('Exporting Partition-1')
while(status.getState()<2): Thread.sleep(100); System.out.print('.')
print('')

status = exportPartition('Partition-2', domain_home)
System.out.print('Exporting Partition-2')
while(status.getState()<2): Thread.sleep(100); System.out.print('.')
print('')

status = exportPartition('Partition-3', domain_home)
System.out.print('Exporting Partition-3')
while(status.getState()<2): Thread.sleep(100); System.out.print('.')
print('')

disconnect()


# Import into production domain
connect('weblogic', 'welcome1', 't3://localhost:8001')

edit()
startEdit()

status = importPartition(domain_home+'/Partition-0.zip')
System.out.print('Importing Partition-0')
while(status.getState()<2): Thread.sleep(100); System.out.print('.')
print('')

status = importPartition(domain_home+'/Partition-1.zip')
System.out.print('Importing Partition-1')
while(status.getState()<2): Thread.sleep(100); System.out.print('.')
print('')

status = importPartition(domain_home+'/Partition-2.zip')
System.out.print('Importing Partition-2')
while(status.getState()<2): Thread.sleep(100); System.out.print('.')
print('')

status = importPartition(domain_home+'/Partition-3.zip')
System.out.print('Importing Partition-3')
while(status.getState()<2): Thread.sleep(100); System.out.print('.')
print('')

activate()


# Start imported partitions
domainRuntime()
cmo.lookupDomainPartitionRuntime('Partition-0').getPartitionLifeCycleRuntime().start()
cmo.lookupDomainPartitionRuntime('Partition-1').getPartitionLifeCycleRuntime().start()
cmo.lookupDomainPartitionRuntime('Partition-2').getPartitionLifeCycleRuntime().start()
cmo.lookupDomainPartitionRuntime('Partition-3').getPartitionLifeCycleRuntime().start()


# Reconfigure targets
edit()
startEdit()

redeploy(appName='RatingService', planPath='../build/plans/RatingServicePlanProd.xml', partition='Partition-0')
redeploy(appName='CustomerService', planPath='../build/plans/CustomerServicePlanProd.xml', partition='Partition-1')
redeploy(appName='FinancialRecordsService', planPath='../build/plans/FinancialRecordsServicePlanProd.xml', partition='Partition-3')
# Redeploy to recreate database
redeploy(appName='BlacklistService', partition='Partition-2')

activate()