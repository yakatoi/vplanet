inp_lst = input().split()
n = int(inp_lst[0])
k = int(inp_lst[1])
str_lst = input().split()
lst  = [int(i) for i in str_lst]

find = 0
give = 0
hasPrint = False

for i in range(len(lst)):
    find+=lst[i]
    if (find>8):
        find-=8
        give+=8
    else:
        give+=find
        find=0
    if give >= k:
        print(i+1)
        hasPrint=True
        break
if not hasPrint:
    print(-1)
