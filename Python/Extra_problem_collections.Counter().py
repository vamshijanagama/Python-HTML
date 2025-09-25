from collections import Counter

n = int(input())
a = list(map(int,input().split()))
b = int(input())
d = Counter(a)
e = 0
for i in range(b):
    c = list(map(int,input().split()))
    if(d[c[0]]>0):
        e = e + c[1]
        d[c[0]] = d[c[0]]-1
print(e)
    
    
    
        
        
    
    
    
    
    
