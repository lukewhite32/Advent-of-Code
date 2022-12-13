
def printIntro():
    import time
    print("This program simulates 10 teams at random play a certain amount of games.")
    print("Each team will increase in difficulty each time they win a game.")
    time.sleep(1)
def getInputs():
    global team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, gameCount
    print("Now enter in all of the team names:")
    team1 = input("Team 1: ")
    team2 = input("Team 2: ")
    team3 = input("Team 3: ")
    team4 = input("Team 4: ")
    team5 = input("Team 5: ")
    team6 = input("Team 6: ")
    team7 = input("Team 7: ")
    team8 = input("Team 8: ")
    team9 = input("Team 9: ")
    team10 = input("Team 10: ")
    gameCount = eval(input("How many times do you want each team playing?"))
    return team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, gameCount
    
def update(team):
    global team1Stats, team2Stats, team3Stats, team4Stats, team5Stats, team6Stats, team7Stats, team8Stats, team9Stats, team10Stats
    team1Stats = 1
    team2Stats = 1
    team3Stats = 1
    team4Stats = 1
    team5Stats = 1
    team6Stats = 1
    team7Stats = 1
    team8Stats = 1
    team9Stats = 1
    team10Stats = 1
    if team == "team1":
        team1Stats = team1Stats + 1
    elif team == "team2":
        team2Stats = team2Stats + 1
    elif team == "team3":
        team3Stats = team3Stats + 1
    elif team == "team4":
        team4Stats = team4Stats + 1
    elif team == "team5":
        team5Stats = team5Stats + 1
    elif team == "team6":
        team6Stats = team6Stats + 1
    elif team == "team7":
        team7Stats = team7Stats + 1
    elif team == "team8":
        team8Stats = team8Stats + 1
    elif team == "team9":
        team9Stats = team9Stats + 1
    elif team == "team1":
        team10Stats = team10Stats + 1
    else:
        pass
    return team1Stats, team2Stats, team3Stats, team4Stats, team5Stats, team6Stats, team7Stats, team8Stats, team9Stats, team10Stats
        
            
def returnGame(teamStats1, teamStats2):
    chance = []
    for x in range(0, teamStats1):
        chance.append("a")
    for x in range(0, teamStats2):
        chance.append("b")
    random.shuffle(chance)
    winner = chance[0]
    return winner
    
    
        
    
def simGames(one, two, three, four, five, six, seven, eight, nine, ten, count):
    import random
    allGames = [[team1Stats, team2Stats], [team1Stats, team3Stats], [team1Stats, team4Stats], [team1Stats, team5Stats],
                    [team1Stats, team6Stats], [team1Stats, team7Stats], [team1Stats, team8Stats], [team1Stats, team9Stats], [team1Stats, team10Stats],
                    [team2Stats, team1Stats], [team2Stats, team3Stats], [team2Stats, team4Stats], [team2Stats, team5Stats], [team2Stats, team6Stats],
                    [team2Stats, team7Stats], [team2Stats, team8Stats], [team2Stats, team9Stats], [team2Stats, team10Stats],
                    [team3Stats, team1Stats], [team3Stats, team2Stats], [team3Stats, team4Stats], [team3Stats, team5Stats],
                    [team3Stats, team6Stats], [team3Stats, team7Stats], [team3Stats, team8Stats], [team3Stats, team9Stats], [team3Stats, team10Stats],
                    [team4Stats, team1Stats], [team4Stats, team2Stats], [team4Stats, team3Stats], [team4Stats, team5Stats], [team4Stats, team6Stats],
                    [team4Stats, team7Stats], [team4Stats, team8Stats], [team4Stats, team9Stats], [team4Stats, team10Stats],
                    [team5Stats, team1Stats], [team5Stats, team2Stats], [team5Stats, team3Stats], [team5Stats, team4Stats], [team5Stats, team6Stats],
                    [team5Stats, team7Stats], [team5Stats, team8Stats], [team5Stats, team9Stats], [team5Stats, team10Stats],
                    [team6Stats, team1Stats], [team6Stats, team2Stats], [team6Stats, team3Stats], [team6Stats, team4Stats], [team6Stats, team5Stats],
                    [team6Stats, team7Stats], [team6Stats, team8Stats], [team6Stats, team9Stats], [team6Stats, team10Stats],
                    [team7Stats, team1Stats], [team7Stats, team2Stats], [team7Stats, team3Stats], [team7Stats, team4Stats],
                    [team7Stats, team5Stats], [team7Stats, team6Stats], [team7Stats, team8Stats], [team7Stats, team9Stats], [team7Stats, team10Stats],
                    [team8Stats, team1Stats], [team8Stats, team2Stats], [team8Stats, team3Stats], [team8Stats, team4Stats], [team8Stats, team5Stats],
                    [team8Stats, team6Stats], [team8Stats, team7Stats], [team8Stats, team9Stats], [team8Stats, team10Stats],
                    [team9Stats, team1Stats], [team9Stats, team2Stats], [team9Stats, team3Stats], [team9Stats, team4Stats], [team9Stats, team5Stats],
                    [team9Stats, team6Stats], [team9Stats, team7Stats], [team9Stats, team8Stats], [team9Stats, team10Stats],
                    [team10Stats, team1Stats], [team10Stats, team2Stats], [team10Stats, team3Stats], [team10Stats, team4Stats], [team10Stats, team5Stats],
                    [team10Stats, team6Stats], [team10Stats, team7Stats], [team10Stats, team8Stats], [team10Stats, team9Stats], ]
    for x in range(0, count):
        for x in range(len(allGames)):
            random.shuffle(allGames)
            returnGame(allGames[x])
            if winner == "a":
                update(allGames[x][0])
            elif winner == "b":
                update(allGames[x][1])
            del(allGames[x])
        allGames = [[team1Stats, team2Stats], [team1Stats, team3Stats], [team1Stats, team4Stats], [team1Stats, team5Stats],
                    [team1Stats, team6Stats], [team1Stats, team7Stats], [team1Stats, team8Stats], [team1Stats, team9Stats], [team1Stats, team10Stats],
                    [team2Stats, team1Stats], [team2Stats, team3Stats], [team2Stats, team4Stats], [team2Stats, team5Stats], [team2Stats, team6Stats],
                    [team2Stats, team7Stats], [team2Stats, team8Stats], [team2Stats, team9Stats], [team2Stats, team10Stats],
                    [team3Stats, team1Stats], [team3Stats, team2Stats], [team3Stats, team4Stats], [team3Stats, team5Stats],
                    [team3Stats, team6Stats], [team3Stats, team7Stats], [team3Stats, team8Stats], [team3Stats, team9Stats], [team3Stats, team10Stats],
                    [team4Stats, team1Stats], [team4Stats, team2Stats], [team4Stats, team3Stats], [team4Stats, team5Stats], [team4Stats, team6Stats],
                    [team4Stats, team7Stats], [team4Stats, team8Stats], [team4Stats, team9Stats], [team4Stats, team10Stats],
                    [team5Stats, team1Stats], [team5Stats, team2Stats], [team5Stats, team3Stats], [team5Stats, team4Stats], [team5Stats, team6Stats],
                    [team5Stats, team7Stats], [team5Stats, team8Stats], [team5Stats, team9Stats], [team5Stats, team10Stats],
                    [team6Stats, team1Stats], [team6Stats, team2Stats], [team6Stats, team3Stats], [team6Stats, team4Stats], [team6Stats, team5Stats],
                    [team6Stats, team7Stats], [team6Stats, team8Stats], [team6Stats, team9Stats], [team6Stats, team10Stats],
                    [team7Stats, team1Stats], [team7Stats, team2Stats], [team7Stats, team3Stats], [team7Stats, team4Stats],
                    [team7Stats, team5Stats], [team7Stats, team6Stats], [team7Stats, team8Stats], [team7Stats, team9Stats], [team7Stats, team10Stats],
                    [team8Stats, team1Stats], [team8Stats, team2Stats], [team8Stats, team3Stats], [team8Stats, team4Stats], [team8Stats, team5Stats],
                    [team8Stats, team6Stats], [team8Stats, team7Stats], [team8Stats, team9Stats], [team8Stats, team10Stats],
                    [team9Stats, team1Stats], [team9Stats, team2Stats], [team9Stats, team3Stats], [team9Stats, team4Stats], [team9Stats, team5Stats],
                    [team9Stats, team6Stats], [team9Stats, team7Stats], [team9Stats, team8Stats], [team9Stats, team10Stats],
                    [team10Stats, team1Stats], [team10Stats, team2Stats], [team10Stats, team3Stats], [team10Stats, team4Stats], [team10Stats, team5Stats],
                    [team10Stats, team6Stats], [team10Stats, team7Stats], [team10Stats, team8Stats], [team10Stats, team9Stats], ]
    
def report(stats1, stats2, stats3, stats4, stats5, stats6, stats7, stats8, stats9, stats10, eam1, eam2, eam3, eam4, eam5, eam6, eam7, eam8, eam9, eam10, gamecnt):
    import time
    print("All games have been simulated. Here are the results: ")
    time.sleep(3)
        
    print(team1, ": " + str(stats1) + "-" + str(stats1-gamecnt))
    print(team2, ": " + str(stats2) + "-" + str(stats2-gamecnt))
    print(team3, ": " + str(stats3) + "-" + str(stats3-gamecnt))
    print(team4, ": " + str(stats4) + "-" + str(stats4-gamecnt))
    print(team5, ": " + str(stats5) + "-" + str(stats5-gamecnt))
    print(team6, ": " + str(stats6) + "-" + str(stats6-gamecnt))
    print(team7, ": " + str(stats7) + "-" + str(stats7-gamecnt))
    print(team8, ": " + str(stats8) + "-" + str(stats8-gamecnt))
    print(team9, ": " + str(stats9) + "-" + str(stats9-gamecnt))
    print(team10, ": " + str(stats10) + "-" + str(stats10-gamecnt))
        
            
    
def init(o, t, th, f, fi, s, se, a, n, tn, coco):
    printIntro()
    getInputs()
    update("poop")
    simGames(team1Stats, team2Stats, team3Stats, team4Stats, team5Stats, team6Stats, team7Stats, team8Stats, team9Stats, team10Stats, gameCount)
    report(team1Stats, team2Stats, team3Stats, team4Stats, team5Stats, team6Stats, team7Stats, team8Stats, team9Stats, team10Stats, team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, gameCount)
        
        
        
    
        
                
        
                    
                    
                    
                    
                    