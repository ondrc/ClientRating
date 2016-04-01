admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")


connect('weblogic',admin_pass)
start('DynamicCluster-0-Server-1', block='true')
start('DynamicCluster-0-Server-2', block='true')
start('otd_DynamicCluster-0-OTD-Config_Example-Machine', block='true')


exit()