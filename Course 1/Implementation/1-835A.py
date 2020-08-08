inp = (input()).split()
s = int(inp[0])
v1 = int(inp[1])
v2 = int(inp[2])
t1 = int(inp[3])
t2 = int(inp[4])
total_one=2*t1+s*v1
total_two=2*t2+s*v2
if total_one==total_two:
   print("Friendship")
elif total_one>total_two:
   print("Second")
else:
   print("First")