def isBet(a, b, c):
    if (c>a and c<b):
        return True
    return False
lst = input().split()
h = float(int(lst[0]))
m = (float(lst[1]))/5
s = (float(lst[2]))/5
a = int(lst[3])
b = int(lst[4])
if (a>b):
    a, b = b, a
m+=s/720
h+=m/12
#print("Output:")
#print(h, m, s, a, b, sep="\n")
count=0
if (isBet(a, b, h)):
    count+=1
if (isBet(a, b, m)):
    count+=1
if (isBet(a, b, s)):
    count+=1
if (count==0 or count==3):
    print("YES")
else:
    print("NO")