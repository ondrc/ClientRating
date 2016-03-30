admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")
domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")
domain_name = os.environ.get("DOMAIN_NAME", "domain")
domain_path = domain_home + '/' + domain_name


# Stop domain
connect('weblogic', admin_pass, 't3://localhost:7001')
shutdown('DynamicCluster-0-LoadBalancer', block='true')
shutdown('DynamicCluster-0','Cluster',block='true')
shutdown('AdminServer', 'Server', 'true', 0, 'true', 'true')

# Shut down node manager
nmConnect('weblogic',admin_pass,'localhost','5556',domain_name,domain_path,'SSL')
stopNodeManager()


exit()