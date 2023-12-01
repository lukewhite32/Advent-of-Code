file = open("allOutcome", "r")
allGames = file.readlines()
score = 0
win = False
draw = False
loss = False
line = 0
rock = False
paper = False
scizzors = False


for x in range(2500):
    if allGames[x][0] == "A":
        if allGames[x][2] == "X":
            loss = True
            scizzors = True
        elif allGames[x][2] == "Y":
            draw = True
            rock = True
        elif allGames[x][2] == "Z":
            win = True
            paper = True
    elif allGames[x][0] == "B":
        if allGames[x][2] == "X":
            loss = True
            rock = True
        elif allGames[x][2] == "Y":
            draw = True
            paper = True
        elif allGames[x][2] == "Z":
            win = True
            scizzors = True
    elif allGames[x][0] == "C":
        if allGames[x][2] == "X":
            loss = True
            paper = True
        elif allGames[x][2] == "Y":
            draw = True
            scizzors = True
        elif allGames[x][2] == "Z":
            win = True
            rock = True
    
    if win:
        score += 6
    elif loss:
        pass
    elif draw:
        score += 3
        
    if rock:
        score += 1
    elif paper:
        score += 2
    elif scizzors:
        score += 3
    
    win = False
    loss = False
    draw = False
    rock = False
    paper = False
    scizzors = False
    
print(score)
