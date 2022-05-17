import json
from loguru import logger
from .meta_driver import MetaDriver

class MetaDriverPsu(MetaDriver):
    """ Abstract Driver with helper class to manage power supply interface
    """

    ###########################################################################
    ###########################################################################

    def push_psu_enable(self, int_value):
        """ To publish the enable status
        """
        payload_dict = {
            "state": int_value
        }
        self.push_attribute("state", json.dumps(payload_dict), retain=True)

    ###########################################################################
    ###########################################################################

    def push_psu_volts(self, float_volts):
        """ To publish the volts value
        """
    
        payload_dict = {
            "volts": float_volts
        }
        self.push_attribute("volts", json.dumps(payload_dict), retain=True)

    ###########################################################################
    ###########################################################################

    def push_psu_amps(self, float_amps):
        """ To publish the amps value
        """
        payload_dict = {
            "amps": float_amps
        }
        self.push_attribute("amps", json.dumps(payload_dict), retain=True)

