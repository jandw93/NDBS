# NDBS 16.0
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

def command(customerID,deviceID,typeID,locationID,listID):
    # Commands containing ftp connection details
    list[0][1] = list[0][1] + '{}:{}@{}{}customer{}-device{}-{}-software'.format(get(customerID,locationID,2),get(customerID,locationID,3),get(customerID,locationID,0),get(customerID,locationID,1),customerID,deviceID,date)
    list[0][2] = list[0][2] + '{}:{}@{}{}customer{}device{}-{}-config'.format(get(customerID,locationID,2),get(customerID,locationID,3),get(customerID,locationID,0),get(customerID,locationID,1),customerID,deviceID,date)
    list[0][3] = list[0][3] + '{}:{}@{}{}customer{}device{}-{}-vlan_dat'.format(get(customerID,locationID,2),get(customerID,locationID,3),get(customerID,locationID,0),get(customerID,locationID,1),customerID,deviceID,date)
    return list[typeID][listID]

def commandlist(typeID):
    return list[typeID]
