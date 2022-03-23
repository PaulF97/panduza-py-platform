#!/usr/bin/python3

from pza_platform import MetaPlatform

###############################################################################
###############################################################################

if __name__ == '__main__':
    
    srv = MetaPlatform()
    srv.register_driver_plugin_discovery()
    srv.run()


