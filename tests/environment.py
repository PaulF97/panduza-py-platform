import time
import shutil
import logging
import subprocess
from behave import *
from steps.xdocz_helpers import PathToRsc

from fixtures.client import client
from fixtures.interface import interface_io

###############################################################################
###############################################################################

def before_tag(context, tag):
    if tag.startswith("fixture.interface.io"):
        name = tag.replace("fixture.interface.io.", "")
        use_fixture(interface_io, context, name=name)
    elif tag.startswith("fixture.client"):
        name = tag.replace("fixture.client.", "")
        use_fixture(client, context, name=name)

###############################################################################
###############################################################################

def before_all(context):
    logging.basicConfig(level=logging.DEBUG)

###############################################################################
###############################################################################

def before_feature(context, feature):

    if feature.name == "Client" or feature.name == "Platform":
        treepath = PathToRsc('platform_tree.json')
        shutil.copyfile(treepath, '/etc/panduza/tree.json')
        subprocess.call(['sudo', 'systemctl', 'restart', 'panduza-py-platform.service'])
        time.sleep(0.5)

    elif feature.name == "Io":
        treepath = PathToRsc('io_tree.json')
        shutil.copyfile(treepath, '/etc/panduza/tree.json')
        subprocess.call(['sudo', 'systemctl', 'restart', 'panduza-py-platform.service'])
        time.sleep(0.5)

###############################################################################
###############################################################################
