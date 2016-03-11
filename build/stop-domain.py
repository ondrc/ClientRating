admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")


# Stop domain
connect('weblogic', admin_pass, 't3://localhost:7001')
shutdown('AdminServer', 'Server', 'true', 0, 'true', 'true')


exit()