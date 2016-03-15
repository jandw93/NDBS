# Module makesshcon

import paramiko, time, os
from connections, logging, commandos import *

def runbck(klantID,deviceID,typeID,locationID,jobID):

    IP = device(klantID,deviceID,3,jobID)
    USN = device(klantID,deviceID,4,jobID)
    PWD = device(klantID,deviceID,5,jobID)
    ENDSW = device(klantID,deviceID,6,jobID)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, port=22, username=USN, password=PWD)
    channel = ssh.invoke_shell()
    channel_bytes = str()

    while True:
        if channel.recv_ready():
            channel_bytes += channel.recv(9999)
            channel_data = channel_bytes.decode("utf-8")
            os.system('cls')
            createlog(3,jobID)

            # View actual output, comment this rule if script is finished.
            # print channel_data
        else:
            createlog(4,jobID)

        for number in range(len(commandlist(typeID))):

            while ENDSW not in channel_data:
                time.sleep(1)

            if 'Address or name of remote host' in channel_data:
                channel.send('\n')
            elif 'Destination filename' in channel_data:
                channel.send('\n')
                createlog(10,jobID)
            elif 'Timed out' in channel_data:
                createlog(0,jobID)
                channel.send('exit')

            channel.send(command(klantID,deviceID,typeID,locationID,number))
            channel.send('\n')

        # datacheck function comes here

            break
