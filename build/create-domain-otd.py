admin_port = int(os.environ.get("ADMIN_PORT", "7001"))
admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")
wl_home = os.environ.get("WL_HOME", "/opt/wls/home/wls/wlserver")
domain_home = os.environ.get("DOMAIN_HOME", "/opt/wls")
domain_name = os.environ.get("DOMAIN_NAME", "domain")


# Setup domain template
setTopologyProfile('Expanded')
selectTemplate('Basic WebLogic Server Domain')
selectTemplate('Oracle Traffic Director - Restricted JRF')
loadTemplates()


# Configure administration server listen port.
cd('Servers/AdminServer')
set('ListenAddress', '')
set('ListenPort', admin_port)
adminServer = cmo


# Define admin user password
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword(admin_pass)


# Set applications directory
setOption("AppDir", domain_home + "/applications")


# Create machine and node manager
cd('/')
create("Example-Machine", "Machine")
cd("/Machines/Example-Machine")
create("Example-Machine-NM", "NodeManager")
cd("NodeManager/Example-Machine-NM")
cmo.setListenAddress('localhost')
cmo.setListenPort(5556)
cmo.setNMType('SSL')


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
cd('/')
domain_path = domain_home + '/' + domain_name
writeDomain(domain_path)
closeTemplate()


exit()