file = open("allCals", "r")
allCal = file.readlines()
totals = []
line = 0
currTotal = 0
for x in range(240):
    while 1:
        if allCal[line] != '\n':
            currTotal += int(allCal[line])
            line += 1
        else:
            break
    totals.append(currTotal)
    currTotal = 0
    line += 1
   

maxReindeerCals = max(totals)
totals.sort()
file.close()