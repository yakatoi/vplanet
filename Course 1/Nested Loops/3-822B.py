nandm = [int(i) for i in input().split()]
nsize = nandm[0]
msize = nandm[1]
n = list(input())
m = list(input())
high = 0
missingbest = []
for i in range(msize-nsize+1):
    counter = 0
    string = m[i:i+nsize]
    missing = [i+1 for i in range(0,nsize)]
    for j in range(len(string)):
        if string[j]==n[j]:
            counter+=1
            missing.remove(j+1)
    if (counter>high):
        missingbest.clear()
        high = counter
        for x in missing:
            missingbest.append(x)
print(nsize-high)
if nsize!=high:
    if len(missingbest)==0 and n!=m :
        print(*[i for i in range(1,nsize+1)])
    else:
        print(*missingbest)