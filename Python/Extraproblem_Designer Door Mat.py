n,k = map(int,input().split(" "))
for i in range(0,n//2):
    a = ".|."
    b = (2*i + 1)*a
    c = ((k)-len(b))//2
    print((c*"-")+b+(c*"-"))
    
m = "WELCOME"
d = (k-len(m))//2
print(d*"-"+m+(d*"-"))
    
for i in range((n//2)-1,-1,-1):
    a = ".|."
    b = (2*i + 1)*a
    c = (k-len(b))//2
    print((c*"-")+b+(c*"-"))
        

        
    
    