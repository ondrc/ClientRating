connect('weblogic', 'welcome1', 't3://localhost:7001')


edit()
startEdit()

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1')
cmo.createJDBCSystemResource('CustomerServiceDS')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS')
cmo.setName('CustomerServiceDS')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCDataSourceParams/CustomerServiceDS')
set('JNDINames',jarray.array([String('jdbc/CustomerServiceDS')], String))

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCDriverParams/CustomerServiceDS')
cmo.setUrl('jdbc:derby:memory:CustomerServiceDB')
cmo.setDriverName('org.apache.derby.jdbc.EmbeddedDriver')
set('PasswordEncrypted','password')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCConnectionPoolParams/CustomerServiceDS')
cmo.setTestTableName('SQL SELECT 1 FROM SYS.SYSTABLES')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCDriverParams/CustomerServiceDS/Properties/CustomerServiceDS')
cmo.createProperty('user')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCDriverParams/CustomerServiceDS/Properties/CustomerServiceDS/Properties/user')
cmo.setValue('CustomerService')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCDriverParams/CustomerServiceDS/Properties/CustomerServiceDS')
cmo.createProperty('create')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCDriverParams/CustomerServiceDS/Properties/CustomerServiceDS/Properties/create')
cmo.setValue('true')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCDriverParams/CustomerServiceDS/Properties/CustomerServiceDS')
cmo.createProperty('databaseName')

cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1/JDBCSystemResources/CustomerServiceDS/JDBCResource/CustomerServiceDS/JDBCDriverParams/CustomerServiceDS/Properties/CustomerServiceDS/Properties/databaseName')
cmo.setValue('CustomerServiceDB')

save()
activate()


edit()
startEdit()

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2')
cmo.createJDBCSystemResource('BlacklistServiceDS')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS')
cmo.setName('BlacklistServiceDS')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCDataSourceParams/BlacklistServiceDS')
set('JNDINames',jarray.array([String('jdbc/BlacklistServiceDS')], String))

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCDriverParams/BlacklistServiceDS')
cmo.setUrl('jdbc:derby:memory:BlacklistServiceDB')
cmo.setDriverName('org.apache.derby.jdbc.EmbeddedDriver')
set('PasswordEncrypted','password')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCConnectionPoolParams/BlacklistServiceDS')
cmo.setTestTableName('SQL SELECT 1 FROM SYS.SYSTABLES')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCDriverParams/BlacklistServiceDS/Properties/BlacklistServiceDS')
cmo.createProperty('user')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCDriverParams/BlacklistServiceDS/Properties/BlacklistServiceDS/Properties/user')
cmo.setValue('BlacklistService')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCDriverParams/BlacklistServiceDS/Properties/BlacklistServiceDS')
cmo.createProperty('create')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCDriverParams/BlacklistServiceDS/Properties/BlacklistServiceDS/Properties/create')
cmo.setValue('true')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCDriverParams/BlacklistServiceDS/Properties/BlacklistServiceDS')
cmo.createProperty('databaseName')

cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2/JDBCSystemResources/BlacklistServiceDS/JDBCResource/BlacklistServiceDS/JDBCDriverParams/BlacklistServiceDS/Properties/BlacklistServiceDS/Properties/databaseName')
cmo.setValue('BlacklistServiceDB')

save()
activate()