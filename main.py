#Main class. Running this will run the following analyses on all the ##_vehicleData files in the current folder:
queueTimeFromVelocity = True
queueLengthFromPosition = True




from QueueLengthFromPosition import *
from QueueTimeFromVelocity import *
import os

if queueTimeFromVelocity:   #Remove totals from old runs
    try:
        os.remove("QueueTimeTotals.txt")
    except OSError:
        pass

if queueLengthFromPosition:
    try:
        os.remove("QueueLengthTotals.txt")
    except OSError:
        pass

for file in os.listdir(os.getcwd()):    #For every file matching *_vehicleData* in current directory
    if '_vehicleData' in file:
        if queueTimeFromVelocity:
            QueueTimeFromVelocity(file)
        if queueLengthFromPosition:
            QueueLengthFromPosition(file)