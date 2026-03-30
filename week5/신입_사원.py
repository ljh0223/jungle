t=int(input())
for _ in range(t):
    n=int(input())
    result=[]
    scores=[tuple(map(int,input().split())) for _ in range(n)]

    scores.sort()
    current=scores[0][1]
    count=1
    
    for score in scores[1:]:
        if score[1]<current:
            current=score[1]
            count+=1
    print(count)