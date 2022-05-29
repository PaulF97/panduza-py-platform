from loguru import logger
from ..meta_driver_psu import MetaDriverPsu
import time

class DriverPsuFake(MetaDriverPsu):
    
    ###########################################################################
    ###########################################################################

    def __init__(self):
        super().__init__()

    def config(self):
        """ From MetaDriver
        """

        return {
            "compatible": "psu_fake",
            "info": { "type": "psu", "version": "1.0" },
        }
    
    ###########################################################################
    ###########################################################################

    def setup(self, tree):
        """ From MetaDriver
        """

        self.supported_settings = self.api_settings.copy()
        self.remove_setting(self.supported_settings, 'serial_port')

        self.api_attributes["volts"]["max"] = 1000
        self.api_attributes["volts"]["scale"] = 0.001

        self.api_attributes["amps"]["max"] = 50
        self.api_attributes["amps"]["scale"] = 0.01
        
        self.api_attributes["model_name"] = "PFPS-SN42 (Panduza Fake Power Supply)"

        if "settings" in tree:
            self.current_settings = tree["settings"].copy()
        else:
            self.current_settings = {}

        self.psu_register_command("state", self.__set_state)
        self.psu_register_command("volts", self.__set_volts)
        self.psu_register_command("amps", self.__set_amps)
        self.psu_register_command("settings", self.__set_settings)

        for i in self.current_settings.copy():
            if i not in self.supported_settings:
                logger.warning("Driver ka3005p does not support setting " + i + " and will ignore it.")
                self.remove_setting(self.current_settings, i)

        self.api_attributes["settings"] = self.supported_settings
        pass

    ###########################################################################
    ###########################################################################

    def on_start(self):
        super().on_start()
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
