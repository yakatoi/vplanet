n = int(input())
count = -1
for i in range(n):
    if (n%(i+1)==0):
        count+=1
print(count)