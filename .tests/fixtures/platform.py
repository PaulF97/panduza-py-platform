import signal
import logging
import threading
import subprocess
from steps.xdocz_helpers import PathToRsc

PLATFORM_PROC=None
PLATFORM_LOGF=None


def start_platform(context):
    """
    """
    global PLATFORM_PROC
    global PLATFORM_LOGF

    # 
    platform_run_script = PathToRsc('pza-py-platform-run.py')
    logging.info(f" >>>> {platform_run_script}")
    PLATFORM_LOGF = open('test_reports/platform_log.txt', 'a')


    PLATFORM_PROC = subprocess.Popen(["python3", platform_run_script], stdout=PLATFORM_LOGF)



def stop_platform(context):
    """
    """
    global PLATFORM_PROC
    logging.info(f" >>>> STOOOP")
    # PLATFORM_PROC.kill()
    PLATFORM_PROC.send_signal(signal.SIGINT)
    PLATFORM_LOGF.close()

