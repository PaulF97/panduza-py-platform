import logging
import threading
import subprocess
from behave import fixture
from steps.xdocz_helpers import PathToRsc




@fixture
def start_platform(context):
    # -- SETUP-FIXTURE PART:

    
    platform_run_script = PathToRsc('pza-py-platform-run.py')
    logging.info(f" >>>> {platform_run_script}")
    logfile = open('logfile', 'w')
    subprocess.run( ["python3", platform_run_script], stdout=logfile)


    # with subprocess.Popen(["python3", platform_run_script], stdout=subprocess.PIPE) as proc:
    #     logfile.write(proc.stdout.read())

    # proc=2
    proc = subprocess.Popen(["python3", platform_run_script], stdout=logfile)
    
        # logfile.write(proc.stdout.read())
    
    # t.start()
    

    # -- CLEANUP-FIXTURE PART:
    # logfile.close()
    # logging.info(f" >>>> CLOSEDD ! !")

    
