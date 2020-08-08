def repl(word, l, r, c1, c2):
    a = word[:l]
    b = word[l:r]
    c = word[r:]
    return a+ b.replace(c1, c2) + c
inp_1 = [int(i) for i in input().split()]
n = inp_1[0]
m = inp_1[1]
word = input()
for i in range(m):
    lst = input().split()
    word = repl(word, int(lst[0])-1, int(lst[1]), lst[2], lst[3])
print(word)