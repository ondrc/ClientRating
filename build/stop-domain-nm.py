admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")
domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")
domain_name = os.environ.get("DOMAIN_NAME", "domain")
domain_path = domain_home + '/' + domain_name


# Stop domain
nmConnect('weblogic',admin_pass,'localhost','5556',domain_name,domain_path,'SSL')
nmKill('AdminServer')
stopNodeManager()


exit()