a = int(input())
b = []
c= {}
for i in range(a):
    n = input()
    b.append(n)
for i in range(len(b)):
    if(b[i] not in c):
        c[b[i]] = 1
    else:
        c[b[i]] = c[b[i]] + 1
        
print(len(c))
print(" ".join(str(x) for x in c.values()))