# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
n,k=map(int,input().split())

coins=[int(input()) for _ in range(n)]
coins.reverse()
count=0
for coin in coins:
    if coin>k:
        continue
    else:
        count+=k//coin
        k%=coin
print(count)