import sys
from loguru import logger
from panduza_platform import MetaPlatform


logger.remove()
logger.add(sys.stdout, format="{level: <10}|{extra[driver_name]: <10}> {message}", level="DEBUG")

srv = MetaPlatform()
srv.force_log = True
srv.register_driver_plugin_discovery()
srv.run()
logger.warning("Platform stopped !")
