n = int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
players=[1, 2]
hasPrint = False
for x in lst:
    if not (x in players):
        print("NO")
        hasPrint = True
        break
    total = [1,2,3]
    total.remove(players[0])
    total.remove(players[1])
    players.clear()
    players.append(x)
    players.append(total[0])
if not hasPrint:
    print("YES")