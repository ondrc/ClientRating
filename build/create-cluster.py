connect('weblogic', 'welcome1', 't3://localhost:7001')
edit()
startEdit()

# Create cluster
dynamicServerTemplate=cmo.createServerTemplate('DynamicCluster-0-ServerTemplate')
dynamicServerTemplate.setListenPort(7000)
dynamicServerTemplateSSL=dynamicServerTemplate.getSSL()
dynamicServerTemplateSSL.setListenPort(8000)

dynCluster=cmo.createCluster('DynamicCluster-0')
dynServers=dynCluster.getDynamicServers()
dynServers.setServerTemplate(dynamicServerTemplate)
dynServers.setServerNamePrefix('DynamicCluster-0-Server-')
#dynServers.setDynamicServerCount(2)
dynServers.setMaximumDynamicServerCount(5)
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
