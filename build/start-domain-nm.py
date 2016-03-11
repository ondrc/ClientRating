admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")
domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")
domain_name = os.environ.get("DOMAIN_NAME", "domain")
domain_path = domain_home + '/' + domain_name
nodemanager_path = domain_path + '/nodemanager'


# Start domain
startNodeManager(NodeManagerHome=nodemanager_path, ListenPort='5556', ListenAddress='localhost')
nmConnect('weblogic',admin_pass,'localhost','5556',domain_name,domain_path,'SSL')
nmStart('AdminServer')


exit()