lst = list(input())
count = 0
for a in range(len(lst)):
    if lst[a]=="Q":
        for b in range(a, len(lst)):
            if lst[b]=="A":
                for c in range(b, len(lst)):
                    if lst[c]=="Q":
                        count+=1
print(count)