import json
from loguru import logger
from .meta_driver import MetaDriver

class MetaDriverPowerSupply(MetaDriver):
    """ Abstract Driver with helper class to manage power supply interface
    """

    ###########################################################################
    ###########################################################################

    def push_power_supply_enable(self, bool_enable):
        """ To publish the enable
        """
        payload_dict = {
            "enable": bool_enable
        }
        self.push_attribute("enable", json.dumps(payload_dict), retain=True)

    ###########################################################################
    ###########################################################################

    def push_power_supply_volts(self, number_volts):
        """ To publish the value
        """
        payload_dict = {
            "volts": number_volts
        }
        self.push_attribute("volts", json.dumps(payload_dict), retain=True)

    ###########################################################################
    ###########################################################################

    def push_power_supply_amps(self, number_amps):
        """ To publish the value
        """
        payload_dict = {
            "amps": number_amps
        }
        self.push_attribute("amps", json.dumps(payload_dict), retain=True)


