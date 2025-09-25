with open("/Users/vamshijanagama/Desktop/Job_preparation/Python/Practice.txt","r+") as f:
    data = f.read()
    b = data.split(",")
    a = 0
    for i in range(len(b)):
        if(int(b[i])%2 == 0):
            a = a+1
    print(a)

    

    
