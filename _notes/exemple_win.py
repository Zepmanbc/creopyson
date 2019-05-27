"""exemple script."""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import creopyson
# import requests
# import json
# import time

IP_CREO = "192.168.56.101"
start_command = "C:/Users/Public/Documents/nitro_proe_remote.bat"
c = creopyson.Client()
current_file = "toto.prt"
drawing_file = "toto.drw"

c.connect()

c.is_creo_running()
