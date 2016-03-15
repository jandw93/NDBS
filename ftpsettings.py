# Module ftpsettings

from logging import *

# Klant ID
# Location ID
# FTP Host
# File path
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

def get(klantID,locationID,listID):
    for i in range(len(settings)):
        if settings[i][0] == klantID and settings[i][1] == locationID:
            result = settings[i][listID]
        else:
            result = 'error'
            createlog(1,jobID)
    return result
