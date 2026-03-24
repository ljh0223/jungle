# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294


""""
n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]

dp=[100001]*(k+1)
dp[0]=0

for coin in coins:
    for i in range(coin,k+1):
        dp[i]=min(dp[i], dp[i-coin]+1)

if dp[k]==100001:
    print(-1)
else:
    print(dp[k])
"""

from collections import deque

n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
visited=[False]*(k+1)
queue=deque([0])
count=0
while queue:
    size=len(queue)

    for _ in range(size):
        now=queue.popleft()
    
        for coin in coins:
            if now+coin==k:
                print(count+1)
                exit()
            elif now+coin<k and visited[now+coin]==False:
                visited[now+coin]=True
                queue.append(coin+now)                
            else:
                continue
    count+=1

print(-1)
    