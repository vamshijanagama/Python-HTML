def swap_case(s):
    results = []
    for i in range(len(s)):
        if(int(ord(s[i]))>=97 and int(ord(s[i]))<=122 or int(ord(s[i]))>=65 and int(ord(s[i]))<=90):
            if(s[i].isupper()):
                results.append(s[i].lower())
            elif(s[i].islower()):
                results.append(s[i].upper())
        else:
            results.append(s[i])
    return "".join(results)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)