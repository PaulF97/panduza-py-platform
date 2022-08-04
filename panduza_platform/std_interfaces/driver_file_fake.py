import time
import threading
from loguru import logger
from ..meta_driver_file import MetaDriverFile

class DriverFileFake(MetaDriverFile):
    
    ###########################################################################
    ###########################################################################

    def config(self):
        """ From MetaDriver
        """
        return {
            "compatible": "file_fake",
            "info": { "type": "file", "version": "1.0" },
            "settings": {
                "behaviour": { "type": "str", "desc": "fake behaviour of the io [static|auto_toggle]" },
                "loopback": { "type": "str", "desc": "to internaly loopback the value to an other fake_io interface" }
            }
        }
    
    ###########################################################################
    ###########################################################################

    def setup(self, tree):
        """ From MetaDriver
        """
        # Initialize basic properties
        self.data = None
        self.mime = None

        # self.behaviour="static"
        # self.__loop = 0
        # self.loopback = None
        # self.mutex = threading.Lock()

        # # Configure the fake behaviour
        # # Static by default => just wait for commands
        # if "settings" in tree:
        #     settings = tree["settings"]

        #     #
        #     if "behaviour" in settings:
        #         target_behaviour = settings["behaviour"]
        #         if target_behaviour in ["static", "auto_toggle"]:
        #             self.behaviour = target_behaviour
        #         else:
        #             logger.error("unknown behaviour '{}' fallback to 'static'", target_behaviour)

        #     # 
        #     if "loopback" in settings:
        #         self.loopback = self.get_interface_instance_from_name(settings["loopback"])
        #         logger.info(f"loopback enabled : {self.loopback}")

        # Register commands
        self.register_command("content/set", self.__content_set)

    ###########################################################################
    ###########################################################################

    def on_start(self):
        """On driver start, just update initiale attributes
        """
        self.push_content(self.data , self.mime)
        
    ###########################################################################
    ###########################################################################

    def loop(self):
        """ From MetaDriver
        """
        return False

    ###########################################################################
    ###########################################################################

    def __content_set(self, payload):
        """Apply set content request
        """
        # Parse request
        req = self.payload_to_dict(payload)
        data_value = req["data"]
        mime_value = req["mime"]

        # Set variables
        self.data = data_value
        self.mime = mime_value

        # Update value
        self.push_content(self.data , self.mime)
        
        # log
        logger.info(f"new content (mime='{mime_value}')")

