domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")


# Export test domain partitions
connect('weblogic', 'welcome1', 't3://localhost:7001')

# exportPartition('Partition-0', domain_home)
# exportPartition('Partition-1', domain_home)
# exportPartition('Partition-2', domain_home)
exportPartition('Partition-3', domain_home)


# Import into production domain
connect('weblogic', 'welcome1', 't3://localhost:8001')

edit()
startEdit()

# importPartition(domain_home+'/Partition-0.zip')
# importPartition(domain_home+'/Partition-1.zip')
# importPartition(domain_home+'/Partition-2.zip')
status=importPartition(domain_home+'/Partition-3.zip')
while(status.getState()==1):pass

activate()


# Start imported partitions
domainRuntime()
# cmo.lookupDomainPartitionRuntime('Partition-0').getPartitionLifeCycleRuntime().start()
# cmo.lookupDomainPartitionRuntime('Partition-1').getPartitionLifeCycleRuntime().start()
# cmo.lookupDomainPartitionRuntime('Partition-2').getPartitionLifeCycleRuntime().start()
cmo.lookupDomainPartitionRuntime('Partition-3').getPartitionLifeCycleRuntime().start()


# Reconfigure targets
edit()
startEdit()

# redeploy(appName='RatingService', planPath='../build/RatingServicePlanProd.xml', partition='Partition-0')
# redeploy(appName='CustomerService', planPath='../build/CustomerServicePlanProd.xml', partition='Partition-1')
redeploy(appName='FinancialRecordsService', planPath='../build/FinancialRecordsServicePlanProd.xml', partition='Partition-3')

activate()