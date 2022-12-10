file = open("allJobs", "r")
allJobs = file.readlines()
total = 0
for x in range(0, len(allJobs)):
    fhours, shours = allJobs[x].split(",")
    frange, srange = fhours.split("-"), shours.split("-")
    if (int(frange[0]) <= int(srange[0]) or int(frange[1]) >= int(srange[1])):
        total += 1
    elif (int(frange[0]) >= int(srange[0]) or int(frange[1]) <= int(srange[1])):
        total += 1
    else:
        pass
print(total) 
