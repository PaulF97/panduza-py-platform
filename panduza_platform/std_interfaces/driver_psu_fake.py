from loguru import logger
from ..meta_driver_psu import MetaDriverPsu
import time

class DriverPsuFake(MetaDriverPsu):
    
    ###########################################################################
    ###########################################################################

    def config(self):
        """ From MetaDriver
        """

        """ Set supported settings to all except serial port """
        self.active_settings = self.api_settings
        self.remove_setting('serial_port')

        self.api_attributes["volts"]["max"] = 1000
        self.api_attributes["volts"]["scale"] = 0.001

        self.api_attributes["amps"]["max"] = 50
        self.api_attributes["amps"]["scale"] = 0.01
        
        self.api_attributes["model_name"] = "PFPS-SN42 (Panduza Fake Power Supply)"

        return {
            "compatible": "psu_fake",
            "info": { "type": "psu", "version": "1.0" },
        }
    
    ###########################################################################
    ###########################################################################

    def setup(self, tree):
        """ From MetaDriver
        """
        MetaDriverPsu.setup(self, tree)
        self.psu_register_command("state", self.__set_state)
        self.psu_register_command("volts", self.__set_volts)
        self.psu_register_command("amps", self.__set_amps)
        self.psu_register_command("settings", self.__set_settings)
        pass

    ###########################################################################
    ###########################################################################

    def on_start(self):
        pass
        
    ###########################################################################
    ###########################################################################

    def __set_state(self, payload):
        """
        """
        # Parse request
        req = self.payload_to_dict(payload)
        req_state = req["state"]
        # Update state
        self.state=req_state
        self.psu_push_attribute("state", self.state)
        logger.info(f"new state :" + str(payload))

    
    ###########################################################################
    ###########################################################################

    def __set_volts(self, payload):
        """
        """
        # Parse request
        req = self.payload_to_dict(payload)
        # Update state
        self.api_attributes["volts"]["value"] = req["volts"]
        self.psu_push_attribute("volts", self.api_attributes["volts"])
        logger.info(f"new volts :" + str(payload))

    ###########################################################################
    ###########################################################################

    def __set_amps(self, payload):
        """
        """
        # Parse request
        req = self.payload_to_dict(payload)
        # Update state
        self.api_attributes["amps"]["value"] = req["amps"]
        self.psu_push_attribute("amps", self.api_attributes["amps"])
        logger.info(f"new amps:" + str(payload))

    ###########################################################################
    ###########################################################################

    def __set_settings(self, payload):
        """
        """
        # Parse request
        req = self.payload_to_dict(payload)
        req_settings = req["settings"]
        # Update state
        self.settings = req_settings
        self.psu_push_attribute("settings", self.settings)
        logger.info(f"new settings:" + str(payload))

    ###########################################################################
    ###########################################################################

    def loop(self):
        """ From MetaDriver
        """
        return False
