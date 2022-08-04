import sys
import argparse
from loguru import logger
from panduza_platform import MetaPlatform


parser = argparse.ArgumentParser()
parser.add_argument('tree', nargs='?', default=None)
args = parser.parse_args()

logger.remove()
logger.add(sys.stdout, format="{level: <10}|{extra[driver_name]: <10}> {message}", level="DEBUG")

srv = MetaPlatform()
srv.force_log = True
srv.register_driver_plugin_discovery()
if args.tree != None:
    srv.load_tree_overide(args.tree)
srv.run()
logger.warning("Platform stopped !")
