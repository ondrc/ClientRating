connect('weblogic', 'welcome1', 't3://localhost:7001')
edit()
startEdit()

# Configure machine
machine=cmo.createUnixMachine('DynamicCluster-0-Machine')
nodeManager=machine.getNodeManager()
nodeManager.setNMType('Plain')
nodeManager.setListenAddress('localhost')
nodeManager.setListenPort(5556)
nodeManager.setDebugEnabled(false)

# Create cluster
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

# Create load balancer server
loadBalancer=cmo.createServer('DynamicCluster-0-LoadBalancer')
loadBalancer.setListenPort(7100)

# Target VirtualTarget-3 to cluster
cd('VirtualTargets/VirtualTarget-3')
cmo.setTargets([dynCluster])

activate()
exit()
