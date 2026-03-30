# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
sol=input().split("-")
answer=sum(map(int,sol[0].split('+')))
for s in sol[1:]:
    answer-=sum(map(int,s.split('+')))

print(answer)