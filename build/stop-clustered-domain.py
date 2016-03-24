admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")


# Stop domain
connect('weblogic', admin_pass, 't3://localhost:7001')
shutdown('DynamicCluster-0-LoadBalancer', block='true')
shutdown('DynamicCluster-0','Cluster',block='true')
shutdown('AdminServer', 'Server', 'true', 0, 'true', 'true')
stopNodeManager()


exit()