# Module connections

from logging import *
# Add items to the list using ['Klant ID','Device ID','Hostname','IP','username','password','commandline endswitch']
# All the Device IDs for every costumer must be unique for the costumers devices, it's no problem to use the same device ID for multiple costumers.

devices = [
# Klant 0 - Device 0
[
'0',
'0'
'hostname.local',
'ipaddress',
'username',
'password',
'hostname.local#'
]
]


def device(klantID,deviceID,listID,jobID):
    for i in range(len(devices)):
        if devices[i][0] == klantID and devices[i][1] == deviceID:
            result = devices[i][listID]
        else:
            result = 'error'
            createlog(5,jobID)
        return result
