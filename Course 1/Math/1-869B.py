ab = [int(i) for i in input().split()]
a = ab[0]
b = ab[1]
ans = 1
hasPrint = False
for i in range(b, a,-1):
    ans*=i%10
    if (ans==0):
        print("0")
        hasPrint=True
        break
if not hasPrint:
    print(ans%10)