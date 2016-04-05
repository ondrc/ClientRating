prod_admin_port = int(os.environ.get("PROD_ADMIN_PORT", "8001"))
admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")
wl_home = os.environ.get("WL_HOME", "/opt/wls/home/wls/wlserver")
domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")
domain_name = os.environ.get("DOMAIN_NAME", "domain")


# Open default domain template
readTemplate(wl_home + "/common/templates/wls/wls.jar")


# Configure administration server listen port.
cd('Servers/AdminServer')
set('ListenAddress', '')
set('ListenPort', prod_admin_port)
adminServer = cmo


# Define admin user password
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword(admin_pass)


# Create virtual targets
cd('/')
create('VirtualTarget-0', 'VirtualTarget')
cd('VirtualTargets/VirtualTarget-0')
cmo.setUriPrefix('/rating-service')
cmo.setTargets([adminServer])

cd('/')
create('VirtualTarget-1', 'VirtualTarget')
cd('VirtualTargets/VirtualTarget-1')
cmo.setUriPrefix('/customer-service')
cmo.setTargets([adminServer])

cd('/')
create('VirtualTarget-2', 'VirtualTarget')
cd('VirtualTargets/VirtualTarget-2')
cmo.setUriPrefix('/blacklist-service')
cmo.setTargets([adminServer])

cd('/')
create('VirtualTarget-3', 'VirtualTarget')
cd('VirtualTargets/VirtualTarget-3')
cmo.setUriPrefix('/records-service')
cmo.setTargets([adminServer])


# Create domain
prod_domain_path = domain_home + '/prod/' + domain_name
writeDomain(prod_domain_path)


exit()