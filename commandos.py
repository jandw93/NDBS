# Module commandos

from ftpsettings import *
import time
date = time.strftime("%Y%m%d-%H%M")

list = [
# TypeID 0 - list[0] - Cisco switch
[
'copy run start',
'archive upload-sw ftp://',
'copy flash:config.text ftp://',
'copy flash:vlan.dat ftp://',
'exit'
],
# Type ID 1 - list[1]
[''],
# Type ID 2 - list[2]
[''],
# Type ID 3 - list[3]
['']
]

def command(klantID,deviceID,typeID,locationID,listID):
    # Commands containing ftp connection details
    list[0][1] = list[0][1] + '{}:{}@{}{}klant{}-device{}-{}-software'.format(get(klantID,locationID,2),get(klantID,locationID,3),get(klantID,locationID,0),get(klantID,locationID,1),klantID,deviceID,date)
    list[0][2] = list[0][2] + '{}:{}@{}{}klant{}device{}-{}-config'.format(get(klantID,locationID,2),get(klantID,locationID,3),get(klantID,locationID,0),get(klantID,locationID,1),klantID,deviceID,date)
    list[0][3] = list[0][3] + '{}:{}@{}{}klant{}device{}-{}-vlan_dat'.format(get(klantID,locationID,2),get(klantID,locationID,3),get(klantID,locationID,0),get(klantID,locationID,1),klantID,deviceID,date)
    return list[typeID][listID]

def commandlist(typeID):
    return list[typeID]
