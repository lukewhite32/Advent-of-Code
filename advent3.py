file = open("allKnapsacks", "r")
allOThem = file.readlines()
total = 0
#for x in range(len(allOThem)):
#    allOThem[x] = allOThem[x][:len(allOThem)-1]  # Gets rid of '/n'
allLet = ['a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z']
allLetters = allLet[0].split(',')
def getCommonLetter(knapsack):
    f = []
    s = []
    for x in range(len(knapsack)):
        if x >= len(knapsack)//2:
            s.append(knapsack[x])
        else:
            f.append(knapsack[x])
            
    for x in range(len(f)):
        for y in range(len(s)):
            if f[x] == s[y]:
                return f[x]
            else:
                pass
            
def getVal(let):
    return allLetters.index(let)

for x in range(len(allOThem)):
    total += allLetters.index(getCommonLetter(allOThem[x]))+1
print(total)
    
    



