connect('weblogic', 'welcome1', 't3://localhost:7001')

edit()
startEdit()
deploy(appName='RatingService', path='../RatingService/target/RatingService-1.0-SNAPSHOT.war', resourceGroup='ResourceGroup-0', partition='Partition-0')
deploy(appName='CustomerService', path='../CustomerService/target/CustomerService-1.0-SNAPSHOT.war', resourceGroup='ResourceGroup-1', partition='Partition-1')
deploy(appName='BlacklistService', path='../BlacklistService/target/BlacklistService-1.0-SNAPSHOT.war', resourceGroup='ResourceGroup-2', partition='Partition-2')
deploy(appName='FinancialRecordsService', path='../FinancialRecordsService/target/FinancialRecordsService-1.0-SNAPSHOT.war', resourceGroup='ResourceGroup-3', partition='Partition-3')
deploy(appName='FinancialRecordsServiceStub', path='../FinancialRecordsServiceStub/target/FinancialRecordsServiceStub-1.0-SNAPSHOT.war', resourceGroup='ResourceGroup-3', partition='Partition-3')
activate()


edit()
startEdit()
redeploy(appName='RatingService', planPath='../build/RatingServicePlan.xml', partition='Partition-0')
redeploy(appName='CustomerService', planPath='../build/CustomerServicePlan.xml', partition='Partition-1')
redeploy(appName='FinancialRecordsService', planPath='../build/FinancialRecordsServicePlan.xml', partition='Partition-3')
activate()