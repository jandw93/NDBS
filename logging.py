# NDBS 16.0
# Module logging

import errorcodes, time

# Get current date and time
date = time.strftime("%d-%m-%Y %H:%M:%S")

# Write errorcode to logfile
def createlog(code,jobID):
    try:
        file = open('NDBS.log','w')
        file.write(date + ' {} '.format(jobID) + errorcodes.error(code))
        file.write('\n')
        file.close()
    except:
        file.close()
