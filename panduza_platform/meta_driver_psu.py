import json
from loguru import logger
from .meta_driver import MetaDriver

class MetaDriverPsu(MetaDriver):
    """ Abstract Driver with helper class to manage power supply interface
    """
    

    def __init__(self):
        self.supported_settings = {}

        self.api_settings = {
            "serial_port": None,
            "ovp": False,
            "ocp": False,
            "silent": False,
            "refresh_period": 0,
        }

        self.api_commands = {
            "state",
            "volts",
            "amps",
            "settings",
        }

        self.api_attributes = {
            "state": "off",
            "volts": {
                "value": 0,
                "min": 0,
                "max": 0,
                "scale": 0
            },
            "amps": {
                "value": 0,
                "min": 0,
                "max": 0,
                "scale": 0
            },
            "model_name": "unknown",
            "settings": {}
        }
    

    def on_start(self):
        self.psu_push_all_attributes()
    
    def psu_register_command(self, name, callback):
        if name not in self.api_commands:
            logger.warning("Driver " + type(self).__name__ + " tried to subscribe to an unofficial command " + name)
        self.register_command_set(name, callback)

    def psu_push_attribute(self, name, data):
        """ To publish an attribute
        """
        if name not in self.api_attributes:
            logger.warning("Driver " + type(self).__name__ + " is publishing an unofficial attribute " + name)
        payload_dict = {
            name: data
        }
        self.api_attributes[name] = data
        self.push_attribute(name, json.dumps(payload_dict), retain=True)

    def psu_push_all_attributes(self):
        print(str(self.api_attributes))
        for key,value in self.api_attributes.items():
            self.psu_push_attribute(key, value)

    def remove_setting(self, list, name):
        list.pop(name, None)