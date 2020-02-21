import datetime


def parseData(textfile):
    data = open(textfile, "r")
    rocketDataStr = data.read()
    
    stateList = ["@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    currentIndex = 0

    for char in rocketDataStr:
        if char in stateList:
            rocketDataStr = rocketDataStr[:currentIndex] + "#" + rocketDataStr[currentIndex:]
            currentIndex = currentIndex + 1
        currentIndex = currentIndex + 1

    rocketDataList = rocketDataStr.split("#")
    rocketDataList.pop(0)
    
    newData = open("parsedata.txt", "w")

    for dataPacket in rocketDataList:
        newData.write(dataPacket)
        newData.write(datetime.datetime.now())
        newData.write("\n")
    
    data.close()
    newData.close()
