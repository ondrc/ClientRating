connect('weblogic', 'welcome1', 't3://localhost:7001')

edit()
startEdit()
deploy(appName='HttpProxy', path='../HttpProxy/target/HttpProxy-1.0-SNAPSHOT.war', targets='DynamicCluster-0-LoadBalancer')
activate()


edit()
startEdit()
redeploy(appName='RatingService', planPath='../build/RatingServicePlanCluster.xml', partition='Partition-0')
redeploy(appName='FinancialRecordsService', planPath='../build/FinancialRecordsServicePlanCluster.xml', partition='Partition-3')
activate()