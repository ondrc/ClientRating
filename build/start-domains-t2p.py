admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")
domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")
domain_name = os.environ.get("DOMAIN_NAME", "domain")
domain_path = domain_home + '/' + domain_name
prod_domain_path = domain_home + '/prod/' + domain_name

# startServer('AdminServer',domain_name,'t3://localhost:7001','weblogic',admin_pass,domain_path,'true',0)
startServer('AdminServer',domain_name,'t3://localhost:8001','weblogic',admin_pass,prod_domain_path,'true',0)

exit()