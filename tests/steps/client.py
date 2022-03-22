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

@Given('a client created with the mqtt test broker url:"{url}" and port:"{port}"')
def step(context, url, port):
    context.pzaconn = Client(url=url, port=int(port))
    AttachTextLog(context, f"Client created with url:'{url}' and port:'{port}'")

###############################################################################
###############################################################################

@Given('aliases from the file:"{file}"')
def step(context, file):
    filepath = PathToRsc(file)
    Core.LoadAliases(filepath=filepath)

###############################################################################
###############################################################################

@Given('a client created with the mqtt test broker alias:"{alias}"')
def step(context, alias):
    context.pzaconn = Client(alias=alias)

###############################################################################
###############################################################################

@When('the client start the connection')
def step(context):
    context.pzaconn.connect()

###############################################################################
###############################################################################

@Then('the client is connected')
def step(context):
    time.sleep(0.5)    
    assert context.pzaconn.is_connected == True




