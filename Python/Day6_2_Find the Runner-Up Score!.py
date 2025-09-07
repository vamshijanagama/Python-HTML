if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = True
    while(a == True):
        a = False
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                a = True
                
    for i in range(len(arr)-1,-1,-1):
        b = arr[-1]
        if(arr[i] != b):
            print(arr[i])
            break