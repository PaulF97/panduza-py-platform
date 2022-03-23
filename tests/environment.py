import shutil
import logging
from behave import *
from steps.xdocz_helpers import PathToRsc

###############################################################################
###############################################################################

def before_all(context):

    logging.basicConfig(level=logging.DEBUG)

    context.DEF_TEST_BROKER_ADDR = "localhost"
    context.DEF_TEST_BROKER_PORT = 1883

###############################################################################
###############################################################################

def before_feature(context, feature):

    if feature.name == "Platform":
        treepath = PathToRsc('tree_test_platform.json')
        shutil.copyfile(treepath, '/etc/panduza/tree.json')

        context.ALIASES = "aliases_test_01.json"
        context.TEST_PLATFORM_ALIAS = "tplat"
        


###############################################################################
###############################################################################
