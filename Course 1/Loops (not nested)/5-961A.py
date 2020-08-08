def isFull(lst):
    for x in lst:
        if x==0:
            return False
    return True

inp_1 = input().split()
n = int(inp_1[0])
m = int(inp_1[1])
row = [0]*n
str_lst = input().split()
lst = [int(i)-1 for i in str_lst]
points = 0
for i in lst:
    row[i]+=1
    if isFull(row):
        points+=1
        row = [i-1 for i in row]
print(points)