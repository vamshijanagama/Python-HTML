if __name__ == '__main__':
    n=[]
    sub = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n.append([name,score])
    
    scores = []
    for s in n:
        scores.append(s[1])

    # remove duplicates and sort
    unique_scores = sorted(set(scores))

    # second lowest score
    second_lowest = unique_scores[1]
    final = []
    for i in n:
        if i[1] == second_lowest:
           final.append(i[0])
    for name in sorted(final):
        print(name)
        
           
    
            
    
    
    