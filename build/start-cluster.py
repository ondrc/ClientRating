admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")
domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")
domain_name = os.environ.get("DOMAIN_NAME", "domain")
domain_path = domain_home + '/' + domain_name
nodemanager_path = domain_path + '/nodemanager'

#startServer('AdminServer',domain_name,'t3://localhost:7001','weblogic',admin_pass,domain_path,'true',0,'false')
#start('DynamicCluster-0','Cluster',block='true')
#start('DynamicCluster-0-LoadBalancer', block='true')


# Start cluster
#startServer('DynamicCluster-0',domain_name,'t3://localhost:7001','weblogic',admin_pass,domain_path,'true',0,'false')
#startServer('DynamicCluster-0-LoadBalancer',domain_name,'t3://localhost:7001','weblogic',admin_pass,domain_path,'true',0,'false')
startNodeManager(NodeManagerHome=nodemanager_path, ListenPort='5556', ListenAddress='localhost')
nmConnect('weblogic',admin_pass,'localhost','5556',domain_name,domain_path,'SSL')
start('DynamicCluster-0','Cluster',block='true')
start('DynamicCluster-0-LoadBalancer', block='true')
#nmStart('DynamicCluster-0',serverType='Cluster')
#nmStart('DynamicCluster-0-LoadBalancer')

exit()