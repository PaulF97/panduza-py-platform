import os
 
# printing environment variables

os.environ["COVERAGE_PROCESS_START"] = os.getcwd() + '/.coveragerc'

print("COVERAGE_PROCESS_START > ", os.environ["COVERAGE_PROCESS_START"])



import coverage
cov = coverage.process_startup()
if not cov:
    print("FAIL COV!")
else:
    print("COV READY")

import sys
from loguru import logger
from panduza_platform import MetaPlatform


logger.remove()
logger.add(sys.stdout, format="{level: <10}> {message}", level="DEBUG")

srv = MetaPlatform()
srv.force_log = True
srv.register_driver_plugin_discovery()
srv.run()
logger.warning("Platform stopped !")
