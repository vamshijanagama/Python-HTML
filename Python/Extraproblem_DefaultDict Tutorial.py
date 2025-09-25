from collections import defaultdict

a,b = map(int,input().split())
d = defaultdict(list)
for i in range(a):
    c = input()
    d[c].append(i+1)
    
for i in range(b):
    e = input()
    if(e in d):
        print(" ".join(str(x) for x in d[e]))
    else:print("-1")
        