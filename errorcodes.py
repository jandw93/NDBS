# NDBS 16.0
# Module errorcodes

list = [
'ERR000: Module makesshcon : A time-out occurred on the SSH-connection.',
'ERR001: Module ftpsettings : The requested FTP setting could not be found.',
'ERR002:',
'ERR003: Module makesshcon : The SSH-connection is succesfully established',
'ERR004: Module makesshcon : An error occured while establishing the SSH-connection.',
'ERR005: Module connections: An undefined device was requested.',
'ERR006:',
'ERR007:',
'ERR008:',
'ERR009:',
'ERR010: Module makesshcon : The command to upload the files with FTP is executed.',
'ERR011:'
]

def error(code):
    return list[code]
