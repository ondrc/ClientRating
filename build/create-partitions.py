connect('weblogic', 'welcome1', 't3://localhost:7001')


edit()
startEdit()


cd('/')
cmo.createPartition('Partition-0')
cd('/Partitions/Partition-0')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-0,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-0,Type=VirtualTarget')], ObjectName))
cmo.createResourceGroup('ResourceGroup-0')
cd('/Partitions/Partition-0/ResourceGroups/ResourceGroup-0')
cmo.setUseDefaultTarget(true)
cmo.setTargets(None)
cmo.findEffectiveTargets()


cd('/')
rgt=cmo.createResourceGroupTemplate('ResourceGroup-1-Template')
cd('/')
cmo.createPartition('Partition-1')
cd('/Partitions/Partition-1')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-1,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-1,Type=VirtualTarget')], ObjectName))
cmo.createResourceGroup('ResourceGroup-1')
cd('/Partitions/Partition-1/ResourceGroups/ResourceGroup-1')
cmo.setResourceGroupTemplate(rgt)
set('Targets', jarray.array([ObjectName('com.bea:Name=VirtualTarget-1,Type=VirtualTarget')], ObjectName))


cd('/')
rgt=cmo.createResourceGroupTemplate('ResourceGroup-2-Template')
cd('/')
cmo.createPartition('Partition-2')
cd('/Partitions/Partition-2')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-2,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-2,Type=VirtualTarget')], ObjectName))
cmo.createResourceGroup('ResourceGroup-2')
cd('/Partitions/Partition-2/ResourceGroups/ResourceGroup-2')
cmo.setResourceGroupTemplate(rgt)
set('Targets', jarray.array([ObjectName('com.bea:Name=VirtualTarget-2,Type=VirtualTarget')], ObjectName))


cd('/')
rgt=cmo.createResourceGroupTemplate('ResourceGroup-3-Template')
cd('/')
cmo.createPartition('Partition-3')
cd('/Partitions/Partition-3')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-3,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VirtualTarget-3,Type=VirtualTarget')], ObjectName))
cmo.createResourceGroup('ResourceGroup-3')
cd('/Partitions/Partition-3/ResourceGroups/ResourceGroup-3')
cmo.setResourceGroupTemplate(rgt)
set('Targets', jarray.array([ObjectName('com.bea:Name=VirtualTarget-3,Type=VirtualTarget')], ObjectName))


save()
activate()


domainRuntime()
cd('/')
cmo.lookupDomainPartitionRuntime('Partition-0').getPartitionLifeCycleRuntime().start()
cmo.lookupDomainPartitionRuntime('Partition-1').getPartitionLifeCycleRuntime().start()
cmo.lookupDomainPartitionRuntime('Partition-2').getPartitionLifeCycleRuntime().start()
cmo.lookupDomainPartitionRuntime('Partition-3').getPartitionLifeCycleRuntime().start()