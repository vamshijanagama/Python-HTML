if __name__ == '__main__':
    N = int(input())
    newlist = []
    for i in range(N):
        n = input().split(" ")
        if(n[0] == "insert"):
            newlist.insert(int(n[1]),int(n[2]))
        elif(n[0] == "print"):
            print(newlist)
        elif(n[0] == "remove"):
            newlist.remove(int(n[1]))
        elif(n[0] == "append"):
            newlist.append(int(n[1]))
        elif(n[0] == "sort"):
            newlist.sort()
        elif(n[0] == "pop"):
            newlist.pop()
        elif(n[0] == "reverse"):
            newlist.reverse()
