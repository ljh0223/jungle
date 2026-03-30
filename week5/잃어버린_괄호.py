sol=input().split("-")
answer=sum(map(int,sol[0].split('+')))
for s in sol[1:]:
    answer-=sum(map(int,s.split('+')))

print(answer)