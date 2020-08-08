n = int(input())
lst = list(input())
l = []
x = 0
y = 0
for dir in lst:
    if (dir=="R"):
        x+=1
    else:
        y+=1
    if (x==y):
        l.append(0)
    elif (x>y):
        l.append(-1)
    else:
        l.append(1)
#print(l)
count = 0
for i in range(1,len(l)-1):
    if l[i]==0:
        if l[i+1]!=l[i-1]:
            count+=1
print(count)
    








