def isBet(one, two, thr):
    (a,b),(c,d),(e,f) = one, two, thr
    x = False
    y = False
    if a==c:
        x=e==a
    elif (a>c):
        if (e>=c and e<=a):
            x = True
    else:
        if (e<=c and e>=a):
            x=True
    if b==d:
        y=f==b
    elif (b>d):
        if (f>=d and f<=b):
            y = True
    else:
        if (f<=d and f>=b):
            y = True
    return x==True and y==True

def perimeter(one, two):
    (a,b), (c,d) = one, two
    x = abs(c-a)+1
    y = abs(d-b)+1
    return 2*x+2*y

nandm = [int(i) for i in input().split()]
n = nandm[0]
m = nandm[1]
ones = []
zeroes = []
for i in range(n):
    inp = list(input())
    for j in range(len(inp)):
        if inp[j]=="1":
            ones.append((j+1, n-i))
        else:
            zeroes.append((j+1, n-i))
#print(ones)
#print(zeroes)
per = 4
for fir in range(len(zeroes)):
    for sec in range(fir+1, len(zeroes)):
        tup1 = zeroes[fir]
        tup2 = zeroes[sec]
        success = True
        for x in ones:
            if isBet(tup1, tup2, x):
                success = False
        if success:
            per = max(per, perimeter(tup1, tup2))
else:
    print(per)