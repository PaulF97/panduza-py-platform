import os
import time
from behave import *
from xdocz_helpers import AttachTextLog, PathToRsc
from panduza import Core, Client

###############################################################################
###############################################################################

# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

###############################################################################
###############################################################################

@Given('io interface "{io_name}" initialized with alias "{io_alias}"')
def step(context, io_name, io_alias):
    context.interfaces["io"][io_name].init(alias=io_alias)

###############################################################################
###############################################################################

@When('io interface "{io_name}" direction is set to "{direction}"')
def step(context, io_name, direction):
    context.interfaces["io"][io_name].direction.set(direction)



