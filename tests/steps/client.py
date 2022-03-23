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
    context.current_test_client = Client(url=url, port=int(port))
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
    context.current_test_client = Client(alias=alias)

###############################################################################
###############################################################################

@Given('a client connected to the default mqtt test broker')
def step(context):
    url = context.DEF_TEST_BROKER_ADDR
    port = context.DEF_TEST_BROKER_PORT
    context.current_test_client = Client(url=url, port=int(port))
    context.current_test_client.connect()
    time.sleep(0.1)    
    assert context.current_test_client.is_connected == True

###############################################################################
###############################################################################

@When('the client start the connection')
def step(context):
    context.current_test_client.connect()

###############################################################################
###############################################################################

@When('the client scan the interfaces')
def step(context):
    context.scanned_interfaces = context.current_test_client.scan_interfaces()
    AttachTextLog(context, f"interfaces: {context.scanned_interfaces}")

###############################################################################
###############################################################################

@Then('the client is connected')
def step(context):
    time.sleep(0.1)
    assert context.current_test_client.is_connected == True

###############################################################################
###############################################################################

@Then('at least a platform interface must be found')
def step(context):
    found_platform = False
    for i in context.scanned_interfaces:
        if context.scanned_interfaces[i]["type"]:
           found_platform = True 
    assert found_platform == True

