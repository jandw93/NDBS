# NDBS 16.0
# Module ftpsettings

from logging import *

# Customer ID
# Location ID
# FTP Host
# File Path
# FTP User
# FTP Password

settings = [
[
'0'
'0'
'ipaddress',
'/filepath/',
'ftpuser',
'password'
]
]

def get(customerID,locationID,listID):
    for i in range(len(settings)):
        if settings[i][0] == customerID and settings[i][1] == locationID:
            result = settings[i][listID]
        else:
            result = 'error'
            createlog(1,jobID)
    return result
