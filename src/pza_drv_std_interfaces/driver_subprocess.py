import time
from loguru import logger
from pza_platform import MetaDriver
import subprocess
import json
import os

class DriverSubprocess(MetaDriver):
    
    ###########################################################################
    ###########################################################################

    def config(self):
        """ From MetaDriver
        """
        return {
            "compatible": "subprocess",
            "info": { "type": "shell", "version": "1.0" }
        }
    
    ###########################################################################
    ###########################################################################

    def setup(self, tree):
        """ From MetaDriver
        """
        self.register_command("run", self.__process_run)

    ###########################################################################
    ###########################################################################

    def loop(self):
        """ From MetaDriver
        """
        return False

    def __push_process_attribute(self, retcode, stdout, stderr):
        msg = {
            "retcode" : retcode,
            "stdout" : stdout,
            "stderr" : stderr
        }
        self.push_attribute("run", json.dumps(msg), retain=True)

    def __process_run(self, payload):
        msg = self.payload_to_dict(payload)
        out = ""
        err = ""
        env = os.environ.copy()
        if msg["env"]:
            for elem in msg["env"]:
                env[elem["key"]] = elem["value"]
        try:
            p = subprocess.Popen(msg["process"].split(), env = env, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            out, err = p.communicate()
            out = out.decode('utf-8')
            err = err.decode('utf-8')
            self.__push_process_attribute(p.returncode, out, err)
        except Exception as e:
            logger.error("{} : {}", msg["process"], str(e))