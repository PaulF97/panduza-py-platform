import os
from behave import *
from xdocz_helpers import AttachTextLog
from panduza import Client

###############################################################################
###############################################################################

# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

###############################################################################
###############################################################################

@Given('a client created with the mqtt test broker url:"{url}" and port:"{port}"')
def step(context, url, port):
    context.pzaconn = Client(url=url, port=int(port))
    AttachTextLog(context, f"Client created with url:'{url}' and port:'{port}'")

###############################################################################
###############################################################################

@When('the client start the connection')
def step(context):
    context.pzaconn.connect()

###############################################################################
###############################################################################

@Then('the client is connected')
def step(context):
    assert context.pzaconn.is_connected == True

