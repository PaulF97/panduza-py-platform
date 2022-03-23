import sys
import serial

from pza_platform import MetaDriver

class DriverStdSerial(MetaDriver):
    
    ###########################################################################
    ###########################################################################

    def config(self):
        return {
            "compatible": "std_serial",
            "info": { "type": "serial", "version": "1.0" }
        }

    ###########################################################################
    ###########################################################################

    def setup(self, tree):
        """
        """
        self.serial_client = None

        port = tree["serial"]["port"]
        baudrate = tree["serial"]["baudrate"]

        # Open the serial connection
        try:
            self.serial_client = serial.Serial(port, baudrate)
        except ValueError as err:
            self.log.error("Cannot open serial port (%s)" % err)
            self.stop()
        except:
            e = sys.exc_info()[0]
            self.log.error("Cannot open serial port (%s)" % e)
            self.stop()


        self.register_command("data/send", self.data_send)
    
    ###########################################################################
    ###########################################################################
        
    def loop(self):
        """
        """
        data = self.rxloop()
        if data:
            self.push_attribute("data", data, retain=False)
            return True
        else:
            return False

    ###########################################################################
    ###########################################################################
    
    def rxloop(self):
        """
        """
        # Is there a client initialized ?
        if not self.serial_client:
            return False

        # Is some data waiting ?
        if not self.serial_client.in_waiting:
            return False

        # Read bytes
        recieved_bytes = self.serial_client.in_waiting
        data = self.serial_client.read(recieved_bytes)
        return data

    ###########################################################################
    ###########################################################################

    def data_send(self, payload):
        # Is there a client initialized ?
        if not self.serial_client:
            self.log.error("Try to send data on closed serial port")
            return

        # Write data
        self.serial_client.write(payload)


