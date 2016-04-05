connect('weblogic', 'welcome1', 't3://localhost:8001')

edit()
startEdit()
deploy(appName='RatingService', path='../RatingService/target/RatingService-1.0-SNAPSHOT.war', resourceGroup='ResourceGroup-0', partition='Partition-0')
deploy(appName='CustomerService', path='../CustomerService/target/CustomerService-1.0-SNAPSHOT.war', resourceGroup='ResourceGroup-1', partition='Partition-1')
deploy(appName='BlacklistService', path='../BlacklistService/target/BlacklistService-1.0-SNAPSHOT.war', resourceGroup='ResourceGroup-2', partition='Partition-2')
activate()


edit()
startEdit()
redeploy(appName='RatingService', planPath='../build/RatingServicePlanProd.xml', partition='Partition-0')
redeploy(appName='CustomerService', planPath='../build/CustomerServicePlanProd.xml', partition='Partition-1')
activate()