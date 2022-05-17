import time
import json
from loguru import logger
from ..meta_driver import MetaDriver

class DriverPlatform(MetaDriver):
    
    ###########################################################################
    ###########################################################################

    def config(self):
        """ From MetaDriver
        """
        return {
            "compatible": "platform_py",
            "info": { "type": "platform", "version": "1.0" }
        }

    ###########################################################################
    ###########################################################################

    def setup(self, tree):
        """ From MetaDriver
        """
        pass

    ###########################################################################
    ###########################################################################

    def on_start(self):
        """ From MetaDriver
        """
        # Push the tree config
        self.push_attribute("tree", json.dumps(self.platform.tree), retain=True)

        # 
        driver_configs = []
        for drv in self.platform.drivers:
            driver_configs.append(drv().config())
        self.push_attribute("drivers", json.dumps(driver_configs), retain=True)


    ###########################################################################
    ###########################################################################

    def loop(self):
        """ From MetaDriver
        """
        return False

