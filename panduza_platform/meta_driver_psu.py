import json
from loguru import logger
from .meta_driver import MetaDriver

class MetaDriverPsu(MetaDriver):
    """ Abstract Driver with helper class to manage power supply interface
    """
    api_settings = {
        "serial_port": "none",
        "ovp": 0,
        "ocp": 0,
        "silent": 0,
        "refresh_period": 0
    }

    api_commands = {
        "state",
        "volts",
        "amps",
        "settings",
    }

    api_attributes = {
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
    
    active_settings = {}
    
    def setup(self, tree):
        self.register_command("init", self.__init)
        pass

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

    def __init(self, payload):
        self.psu_push_all_attributes()

    def psu_push_all_attributes(self):
        """ To publish an attribute
        """
        for name,value in self.api_attributes.items():
            self.psu_push_attribute(name, value)

    def remove_setting(self, name):
        self.active_settings.pop(name, None)