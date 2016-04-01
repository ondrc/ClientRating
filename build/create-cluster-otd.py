connect('weblogic', 'welcome1', 't3://localhost:7001')
edit()
startEdit()

# Get machine
machine=cd("/Machines/Example-Machine")

# Create cluster
cd('/')
dynamicServerTemplate=cmo.createServerTemplate('DynamicCluster-0-ServerTemplate')
dynamicServerTemplate.setListenPort(7100)
dynamicServerTemplate.setMachine(machine)
dynamicServerTemplateSSL=dynamicServerTemplate.getSSL()
dynamicServerTemplateSSL.setListenPort(8100)

dynCluster=cmo.createCluster('DynamicCluster-0')
dynServers=dynCluster.getDynamicServers()
dynServers.setServerTemplate(dynamicServerTemplate)
dynServers.setServerNamePrefix('DynamicCluster-0-Server-')
dynServers.setDynamicClusterSize(2)
dynServers.setMaxDynamicClusterSize(5)
dynServers.setCalculatedListenPorts(true)
dynServers.setCalculatedMachineNames(true)

# Target VirtualTarget-3 to cluster
cd('VirtualTargets/VirtualTarget-3')
cmo.setTargets([dynCluster])

activate()
editCustom()
startEdit()

# Configure Oracle Traffic Director
otd_createConfiguration({'configuration':'DynamicCluster-0-OTD-Config', 'server-name':'localhost', 'listener-port':'7100', 'origin-server':'localhost:7101'})
otd_createInstance({'configuration':'DynamicCluster-0-OTD-Config', 'machine':'Example-Machine'})
otd_setHealthCheckProperties({'configuration':'DynamicCluster-0-OTD-Config', 'origin-server-pool':'origin-server-pool-1', 'dynamic-server-discovery':'true'})

activate()
exit()
