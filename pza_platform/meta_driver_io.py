import json
from loguru import logger
from pza_platform import MetaDriver

class MetaDriverIo(MetaDriver):
    """ Abstract Driver with helper class to manage io interface
    """

    ###########################################################################
    ###########################################################################

    def push_io_value(self, int_value):
        """ To publish the value
        """
        payload_dict = {
            "value": int_value
        }
        self.push_attribute("value", json.dumps(payload_dict), retain=True)

    ###########################################################################
    ###########################################################################

    def push_io_direction(self, str_direction):
        """ To publish the value
        """
        if str_direction != 'in' and str_direction != 'out':
            raise Exception("Direction must be 'in' or 'out'")

        payload_dict = {
            "direction": str_direction
        }
        self.push_attribute("direction", json.dumps(payload_dict), retain=True)

