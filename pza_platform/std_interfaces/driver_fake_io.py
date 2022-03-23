import time
from loguru import logger
from pza_platform import MetaDriverIo

class DriverFakeIo(MetaDriverIo):
    
    ###########################################################################
    ###########################################################################

    def config(self):
        """ From MetaDriver
        """
        return {
            "compatible": "fake_io",
            "info": { "type": "io", "version": "1.0" }
        }
    
    ###########################################################################
    ###########################################################################

    def value_set(self, payload):
        """ Apply set value request
        """
        # Parse request
        req = self.payload_to_dict(payload)
        req_value = req["value"]
        # Update value
        self.value=req_value
        self.push_io_value(self.value)
        # log
        logger.info(f"new value : {self.value}")

    ###########################################################################
    ###########################################################################

    def direction_set(self, payload):
        """
        """
        # Parse request
        req = self.payload_to_dict(payload)
        req_direction = req["direction"]
        # Update direction
        self.direction=req_direction
        self.push_io_direction(self.direction)
        # log
        logger.info(f"new direction : {self.direction}")

    ###########################################################################
    ###########################################################################

    def setup(self, tree):
        """ From MetaDriver
        """
        # Configure the fake behaviour
        # Static by default => just wait for commands
        self.behaviour="static"
        if "behaviour" in tree["gpio"]:
            target_behaviour=tree["gpio"]["behaviour"]
            if target_behaviour in ["static", "auto_toggle"]:
                self.behaviour = target_behaviour
            else:
                logger.error("unknown behaviour '{}' fallback to 'static'", target_behaviour)

        # Initialize basic properties
        self.direction = 'in'
        self.value=0

        #
        self.__loop = 0

        # Register commands
        self.register_command("value/set", self.value_set)
        self.register_command("direction/set", self.direction_set)
        
        #
        self.push_io_value(self.value)

    ###########################################################################
    ###########################################################################

    def loop(self):
        """ From MetaDriver
        """
        if self.behaviour == "auto_toggle":
            if self.__loop >= 8:
                self.value = (self.value + 1) % 2
                self.push_io_value(self.value)
                self.__loop = 0
            self.__loop += 1
            time.sleep(0.25)
            return True
        else:
            return False
