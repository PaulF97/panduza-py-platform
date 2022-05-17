import time
from loguru import logger
from ..meta_driver_psu import MetaDriverPsu

class DriverPsuFake(MetaDriverPsu):
    
    ###########################################################################
    ###########################################################################

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

        self.register_command("state/set", self.__set_state)
        self.register_command("volts/set", self.__set_volts)
        self.register_command("amps/set", self.__set_amps)


    ###########################################################################
    ###########################################################################

    def on_start(self):
        pass

    def __set_state(self, payload):
        """
        """
        # Parse request
        req = self.payload_to_dict(payload)
        req_enable = req["state"]
        # Update enable
        self.enable=req_enable
        self.push_psu_enable(self.enable)
        logger.info(f"new state :" + str(payload))
    
    ###########################################################################
    ###########################################################################

    def __set_volts(self, payload):
        """
        """
        # Parse request
        req = self.payload_to_dict(payload)
        req_volts = req["volts"]
        # Update enable
        self.volts=req_volts
        self.push_psu_volts(self.volts)
        logger.info(f"new volts :" + str(payload))

    ###########################################################################
    ###########################################################################

    def __set_amps(self, payload):
        """
        """
        # Parse request
        req = self.payload_to_dict(payload)
        req_amps = req["amps"]
        # Update enable
        self.amps=req_amps
        self.push_psu_amps(self.amps)
        logger.info(f"new amps:" + str(payload))

    ###########################################################################
    ###########################################################################

    def loop(self):
        """ From MetaDriver
        """
        return False
