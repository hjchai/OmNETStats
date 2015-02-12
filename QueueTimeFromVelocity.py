# From an input file, outputs:
# <filenum>_QueueTimePerVehicle.txt, with each vehicle's name, total time alive, and percent of its time spent stationary (velocity < 0.01).
# Appends to QueueTimeTotals.txt the file name, followed by total time alive and percent time stationary of all vehicles

from QueueLengthFromPosition import leadingInt

class Vehicle:  #Tracks total existence time vs paused time
    def __init__(self, name):
        self.name = name
        self.timeTotal = 0
        self.timePaused = 0

def QueueTimeFromVelocity(fileName, path):
    filePrefix = fileName[:-16]
    vehiclesDict = {}   #Map names to vehicles
    with open(path + fileName, 'rt') as inFile, open(path + filePrefix  + '_QueueTimePerVehicle.txt', 'wt') as queueTimes, open(path + 'QueueTimeTotals.txt', 'a') as queueTotals:
        next(inFile)    #Skip header
        for row in inFile:
            if row.strip(): #Skip blank rows
                row = row.split()

                name = row[2]
                if name not in vehiclesDict:    #Make sure this object exists
                    vehiclesDict[name] = Vehicle(name)

                vehicle = vehiclesDict[name]
                vehicle.timeTotal += 1  #Add to total time, and paused time if it's paused
                speed = float(row[6])
                if speed < 0.01:
                    vehicle.timePaused += 1
        timeTotal = 0   #Total times for all vehicles
        timePaused = 0
        for k in sorted(vehiclesDict, key=len): #Print each vehicle's data and add it to the total
            #print(vehicle.name + ": " + str(float(vehicle.timePaused)/vehicle.timeTotal))
            vehicle = vehiclesDict[k]
            timeTotal += vehicle.timeTotal
            timePaused += vehicle.timePaused
            queueTimes.write(k + " " + str(vehicle.timeTotal) + " " + str(timePaused / timeTotal) + "\n")
        total = float(timePaused)/timeTotal
        print(fileName + " " + str(timeTotal) + " " + str(total))
        queueTotals.write(fileName + " " + str(timeTotal) + " " + str(total) + "\n")
    return total
