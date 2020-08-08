n = int(input())
count = 0
for a in range(1,n+1):
    for b in range(a+1, n+1):
            count += b < a^b < min(a+b, n+1)
print(count)
