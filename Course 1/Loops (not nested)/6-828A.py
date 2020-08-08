inp = [int(i) for i in input().split()]
n = inp[0]
a = inp[1]
b = inp[2]
lst = [int(i) for i in input().split()]
count = 0
num2 = 0
for x in lst:
    if x==1:
        if a>0:
            a-=1
        elif b>0:
            b-=1
            num2+=1
        elif num2>0:
            num2-=1
        else:
            count+=1
    else:
        if b>0:
            b-=1
        else:
            count+=2
print(count)