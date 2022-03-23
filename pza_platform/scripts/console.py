from pza_platform import MetaPlatform


SERVICE_FILE_CONTENT = "\
[Unit] \
Description=Platform Python to support Panduza Meta Drivers \
After=network.target \
\
[Service]  \
ExecStart=pza-py-platform-run \
\
[Install] \
WantedBy=multi-user.target \
"

###############################################################################
###############################################################################

def install_service():
    print("install in /etc/systemd/system")
    f = open("/etc/systemd/system/panduza-py-platform.service", "x")
    f.write(SERVICE_FILE_CONTENT)
    f.close()

###############################################################################
###############################################################################

def run_platform():
    srv = MetaPlatform()
    srv.force_log = False
    srv.register_driver_plugin_discovery()
    srv.run()

###############################################################################
###############################################################################
