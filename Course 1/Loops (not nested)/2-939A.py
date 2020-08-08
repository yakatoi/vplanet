n = int(input())
str_lst = input().split()
lst = [int(i) for i in str_lst]
#print(lst)
hasPrint = False
for i in range(len(lst)):
    a = lst[i]
    b = lst[a-1]
    c = lst[b-1]
    if (c==i+1):
        print("YES")
        hasPrint=True
        break
if not hasPrint:
    print("NO")

    