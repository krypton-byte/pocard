import json
import os
from os.path import dirname
ASSETS_DIR = dirname(__file__)+"/assets"
FONT = dirname(__file__)+"/font/solid.ttf"
FONT2 = dirname(__file__)+"/font/desc.ttf"
TEMPLATE =json.loads(open(dirname(__file__)+"/template.json").read())