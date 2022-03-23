from behave import *
from xdocz_helpers import AttachTextLog, PathToRsc

###############################################################################
###############################################################################

# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

###############################################################################
###############################################################################

@Given('the alias file "{filepath}" loaded')
def step(context, filepath):
    # context.current_test_client = Client(url=url, port=int(port))
    AttachTextLog(context, f"Client created with url:'{filepath}'")

