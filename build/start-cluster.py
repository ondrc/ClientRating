admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")
domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")
domain_name = os.environ.get("DOMAIN_NAME", "domain")
domain_path = domain_home + '/' + domain_name
nodemanager_path = domain_path + '/nodemanager'


# Start Node Manager
connect('weblogic',admin_pass)
startNodeManager(NodeManagerHome=nodemanager_path, ListenPort='5556', ListenAddress='localhost', NativeVersionEnabled='false', block='true', username='weblogic', password=admin_pass, domainName=domain_name)

# Start cluster
start('DynamicCluster-0-Server-1', block='true')
start('DynamicCluster-0-Server-2', block='true')
start('DynamicCluster-0-LoadBalancer', block='true')


exit()