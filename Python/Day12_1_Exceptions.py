t = int(input())  # number of test cases
for i in range(t):
    try:
        x, y = map(int, input().split())
        print(x // y)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
