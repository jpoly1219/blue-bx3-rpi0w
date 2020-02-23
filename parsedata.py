"""
parsedata.py is basically a module that provides a single function parseData().
The function accepts one parameter, "textfile", which is a file that the function
will write to. The function will split the string of data when the rocket's flight state
changes (shown as a single ASCII character in the list stateList). This function is 
crucial, as the maincontrol.py only accepts rocket's flight data as a single bytestring, 
and has no way of knowing when new data is updated.
"""


def parseData(textfile):
    data = open(textfile, "r")
    rocketDataStr = data.read()
    
    stateList = ["@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
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
        newData.write("\n")
    
    data.close()
    newData.close()
