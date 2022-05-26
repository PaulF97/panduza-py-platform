import abc
import sys
import time
import json
import logging
import threading
import paho.mqtt.client as mqtt

from loguru import logger

class MetaDriver(metaclass=abc.ABCMeta):


    ###########################################################################
    ###########################################################################

    def __init__(self):
        """
        Constructor
        """
        pass

    ###########################################################################
    ###########################################################################

    def initialize(self, platform, machine, broker, tree):
        """
        """
        #  \todo assert if info not present
        #  \todo assert if name not present

        self.platform = platform
        self.machine = machine
        self.broker = broker
        self.tree = tree
        self.name = self.tree["name"]
        self.log = logging.getLogger("pza.driver." + self.name)
        self.info = json.dumps( self.config()["info"] )
        self.commands = {}
        self.base_topic = "pza/" + machine + "/" + self.tree["driver"] + "/" + self.name
        self.base_topic_size = len(self.base_topic)
        self.base_topic_cmds = self.base_topic + "/cmds/"
        self.base_topic_cmds_size = len(self.base_topic_cmds)
        self.base_topic_atts = self.base_topic + "/atts/"
        self.base_topic_atts_size = len(self.base_topic_atts)


    ###########################################################################
    ###########################################################################

    def __load_commands(self):
        """
        """
        self.log.debug(" + load commands")
        for cmd in self.commands:
            cmd_topic = self.base_topic_cmds + cmd
            self.log.debug("      '%s' -----> [%s]", cmd, cmd_topic)
            self.mqtt_client.subscribe(cmd_topic)

    ###########################################################################
    ###########################################################################

    def __alive(self):
        """
        """
        tick=0
        while self.alive:
            if tick % 4 == 0:

                self.mqtt_client.publish(self.base_topic + "/info", self.info, retain=False)
            tick += 1
            time.sleep(0.5)

    ###########################################################################
    ###########################################################################

    def start(self):
        """
        """
        # Mqtt connection
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_message = self.__on_message

        try:
            # Keep alive flag
            self.alive = True

            # Start connection
            self.mqtt_client.connect(self.broker.addr, self.broker.port)

            #
            self.alive_thread = threading.Thread(target=self.__alive)
            self.alive_thread.start()

            # Start the mqtt client
            self.mqtt_client.loop_start()

            #
            self.__load_commands()

            #
            self.on_start()

            # Main loop
            self.log.debug("Interface started...")
            while self.alive:
                if not self.loop():
                    time.sleep(0.1)

        # except AttributeError as err:
        #     mog.error("Critical error on the serial interface %s (%s)" % (self.name, err))
        # except ConnectionRefusedError as err:
        #     mog.error("Critical error on the driver, MQTT connection failed %s (%s)" % (self.name, err))
        #     mog.error("- you can check if the port %d is open on the broker %s" % (self.bridge.port, self.bridge.port))
        except:
            e = sys.exc_info()[0]
            self.log.exception("Critical error on driver %s (%s)" % (self.name, e))

        # Info
        logger.info("Interface '{}' stopped !", self.name)

    ###########################################################################
    ###########################################################################
    
    def __on_message(self, client, userdata, msg):
        """
        Callback to manage incomming mqtt messages
        """
        topic_string = str(msg.topic)
        suffix = topic_string[self.base_topic_cmds_size:]
        if suffix in self.commands:
            self.commands[suffix](msg.payload)

    ###########################################################################
    ###########################################################################

    def stop(self):
        """
        """
        # Keep alive flag
        self.alive = False
        self.alive_thread.join()

    ###########################################################################
    ###########################################################################

    def register_command(self, topic_cmds_suffix, callback):
        """
        """
        self.commands[topic_cmds_suffix] = callback

    ###########################################################################
    ###########################################################################

    def register_command_set(self, topic_cmds_suffix, callback):
        """
        """
        self.commands[topic_cmds_suffix + "/set"] = callback

    ###########################################################################
    ###########################################################################

    def push_attribute(self, topic_atts_suffix, payload, qos = 0, retain = False):
        """
        """
        self.mqtt_client.publish(self.base_topic_atts + topic_atts_suffix, payload, qos=qos, retain=retain)

    ###########################################################################
    ###########################################################################

    def payload_to_dict(self, payload):
        """ To parse json payload
        """
        return json.loads(payload.decode("utf-8"))

    ###########################################################################
    ###########################################################################

    def payload_to_int(self, payload):
        """
        """
        return int(payload.decode("utf-8"))

    ###########################################################################
    ###########################################################################

    def payload_to_str(self, payload):
        """
        """
        return payload.decode("utf-8")

    ###########################################################################
    ###########################################################################

    def get_interface_instance_from_name(self, name):
        """
        """
        return self.platform.get_interface_instance_from_name(name)

    ###########################################################################
    ###########################################################################

    def initial_setup(self):
        """To ease the interface initialisation
        """
        self.setup(self.tree)

    ###########################################################################
    ###########################################################################

    @abc.abstractmethod
    def config(self):
        """
        """
        pass

    ###########################################################################
    ###########################################################################

    @abc.abstractmethod
    def setup(self, tree):
        """Mono-threaded initialization of the interface

        Warning mqtt client is not initialized at this step
        """
        pass

    ###########################################################################
    ###########################################################################

    # @abc.abstractmethod
    def on_start(self):
        """
        """
        pass

    ###########################################################################
    ###########################################################################

    @abc.abstractmethod
    def loop(self):
        """
        """
        return False

