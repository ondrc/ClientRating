admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")


# Stop domains
connect('weblogic', admin_pass, 't3://localhost:7001')
shutdown('AdminServer', 'Server', 'true', 0, 'true', 'true')
connect('weblogic', admin_pass, 't3://localhost:8001')
shutdown('AdminServer', 'Server', 'true', 0, 'true', 'true')


exit()