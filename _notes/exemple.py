"""exemple script."""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import creopyson
# import requests
# import json
import time

IP_CREO = "192.168.56.101"
IP_CREO = "192.168.0.38"
start_command = "C:/Users/Public/Documents/nitro_proe_remote.bat"
c = creopyson.Client(ip_adress=IP_CREO)
current_file = "toto.prt"
drawing_file = "toto.drw"

c.connect()
# c.is_creo_running()
# c.creo_cd("D:/CAO/")

# listfiles = c.creo_list_files()
# listdirs = c.creo_list_dirs()
c.is_creo_running()
if not c.is_creo_running():
    c.start_creo(start_command)
    # running = c.is_creo_running()
    # while running:
    #     running = c.is_creo_running()
    #     print(running)
    #     time.sleep(1)
    #     wait = wait + 1
    #     print(wait)
    # print("creo is running...")

# c.file_open(["toto.prt", "toto.drw"], display=True, activate=False)

wait = 0
print("opening file...")
while not c.file_open(current_file, display=True):
    c.is_creo_running()
    time.sleep(1)
    wait = wait + 1
    print(wait)
    if wait >= 30:
        exit("too long...")

if c.file_exists(current_file):
    c.dimension_set(current_file, "diamm", 180)
    try:
        c.file_regenerate(current_file)
    except Warning:
        c.dimension_set(current_file, "diamm", 50)
        c.file_regenerate(current_file)

# current_file = "toto.asm"
# c.file_open(current_file)
# c.bom_get_paths()
exit()

c.file_open(drawing_file, new_window=True)
if c.file_exists(drawing_file):
    print(c.interface_export_pdf(drawing_file))

# c.stop_creo()

# c.disconnect()

# c.kill_creo()
# c.stop_creo()

# c.disconnect()
# c.is_creo_running
# c.kill_creo
# c.start_creo
# c.stop_creo

# c.bom.get_paths

# c.dimension.copy
# c.dimension.list_detail
# c.dimension.list
# c.dimension.set
# c.dimension.show
# c.dimension.user_select


# print(c.sessionId)

print("Done")
