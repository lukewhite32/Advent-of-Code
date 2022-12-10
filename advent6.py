file = open("allPackage", "r")
package = file.readlines()

def createList(string):
    tmpLst = []
    for x in range(len(string)):
        tmpLst.append(string[x])
    return tmpLst

def isRepeat(data):
    for x in range(14):
        dataCheck = createList(data)
        del(dataCheck[x])
        if data[x] in dataCheck:
            return True
        else:
            pass
    return False

for x in range(len(package[0])):
    if isRepeat(package[0][x]+package[0][x+1]+package[0][x+2]+package[0][x+3]+package[0][x+4]+package[0][x+5]+package[0][x+6]+package[0][x+7]+package[0][x+8]+package[0][x+9]+package[0][x+10]+package[0][x+11]+package[0][x+12]+package[0][x+13]):
        pass
        
    else:
        print(x+14)
        break
    