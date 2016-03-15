# Module logging

import foutcodes, time
date = time.strftime("%d-%m-%Y %H:%M:%S")

def createlog(code,jobID):
    try:
        file = open('NDBS.log','w')
        file.write(date + ' {} '.format(jobID) + foutcodes.foutcode(code))
        file.write('\n')
        file.close()
    except:
        file.close()

#file = open('NDBS.log','r')

#for line in file:
#    do something
