file = open("allInstructions", "r")
allInst = file.readlines()
slots = [['F', 'R', 'W'], ['P', 'W', 'V', 'D', 'C', 'M', 'H', 'T'], ['L', 'N', 'Z', 'M', 'P'], ['R', 'H', 'C', 'J'], ['B', 'T', 'Q', 'H', 'G', 'P', 'C'], ['Z', 'F', 'L', 'W', 'C', 'G'], ['C', 'G', 'J', 'Z', 'Q', 'L', 'V', 'W'], ['C', 'V', 'T', 'W', 'F', 'R', 'N', 'P'], ['V', 'S', 'R', 'G', 'H', 'W', 'K']]

def move(amt, fro, to):
    for x in range(0, amt):
        slots[to-1].insert(x, str(slots[fro-1][0]))
        del(slots[fro-1][0])
        
def findTop(slot):
    return slots[slot][0]

for x in range(len(allInst)):
    move(int(allInst[x].split(" ")[1]), int(allInst[x].split(" ")[3]), int(allInst[x].split(" ")[5]))
    
    
for x in range(9):
    print(findTop(x))
    