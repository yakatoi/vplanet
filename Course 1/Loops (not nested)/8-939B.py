inp1 = [int(i) for i in input().split()]
n = inp1[0]
k = inp1[1]
lst = [int(i) for i in input().split()]
rem = [n%i for i in lst]
index = rem.index((min(rem)))
print(index+1, n//lst[index])