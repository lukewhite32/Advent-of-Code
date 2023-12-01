file = open("allDirec", "r")
allDirec = ['$ cd /', 
'$ ls', 
'dir a', 
'14848514 b.txt', 
'8504156 c.dat', 
'dir d', 
'$ cd a', 
'$ ls', 
'dir e', 
'29116 f', 
'2557 g', 
'62596 h.lst', 
'$ cd e', 
'$ ls', 
'584 i', 
'$ cd ..', 
'$ cd ..', 
'$ cd d', 
'$ ls', 
'4060174 j', 
'8033020 d.log', 
'5626152 d.ext', 
'7214296 k']

files = []
fileLength = 0
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for x in range(len(allDirec)):
    if allDirec[x][0] == "$":
        pass
    
    elif allDirec[x][0] in num:
        spl = allDirec[x].split()
        if spl[1] in files:
            pass
        else:
            if int(spl[0]) >= 100000:
                fileLength += int(spl[0])
                files.append(spl[1])

