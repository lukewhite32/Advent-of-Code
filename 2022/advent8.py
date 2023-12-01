file = open("allTrees", "r")
allTrees = file.readlines()
for x in range(len(allTrees)):
    allTrees[x] = allTrees[x][:len(allTrees)-1]

vis = 0
length = len(allTrees[0])
def up(locX, locY):
    return allTrees[locY+1][locX]
def down(locX, locY):
    return allTrees[locY-1][locX]
def left(locX, locY):
    return allTrees[locY][locX-1]
def right(locX, locY):
    return allTrees[locY][locX+1]
def getCoords(locX, locY):
    return allTrees[locX][locY]
for x in range(len(allTrees)):
    if x == 0:
        vis += length
    elif x == len(allTrees)-1:
        vis += length
    else:
        vis += 2

def isHidden(x, y):
    coords = int(getCoords(x, y))
    
    if int(left(x, y)) >= coords and int(right(x, y)) >= coords:
        
        return True
    else:
        return False


for x in range(1, len(allTrees)-1):
    for y in range(1, length-1):
        if not isHidden(int(y), int(x)):
            vis += 1
        else:
            pass

