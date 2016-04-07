domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")


# Export test domain partitions
connect('weblogic', 'welcome1', 't3://localhost:7001')

exportPartition('Partition-0', domain_home)
exportPartition('Partition-1', domain_home)
exportPartition('Partition-2', domain_home)
exportPartition('Partition-3', domain_home)

disconnect()


# Import into production domain
connect('weblogic', 'welcome1', 't3://localhost:8001')

edit()
startEdit()

status_1=importPartition(domain_home+'/Partition-0.zip')
System.out.print('Migrating Partition-0')
while(status_1.getState()==1):Thread.sleep(100);System.out.print('.')
print('')
status_2=importPartition(domain_home+'/Partition-1.zip')
System.out.print('Migrating Partition-1')
while(status_2.getState()==1):Thread.sleep(100);System.out.print('.')
print('')
status_3=importPartition(domain_home+'/Partition-2.zip')
System.out.print('Migrating Partition-2')
while(status_3.getState()==1):Thread.sleep(100);System.out.print('.')
print('')
status_4=importPartition(domain_home+'/Partition-3.zip')
System.out.print('Migrating Partition-3')
while(status_4.getState()==1):Thread.sleep(100);System.out.print('.')
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