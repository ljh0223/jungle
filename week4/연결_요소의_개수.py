from collections import deque

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)
count=0
visit=[False]*(n+1)

# def dfs(start):
#     visited[start]=True
#     for nxt in graph[start]:
#         if visited[nxt]==False:
#             visited[nxt]=True
#             dfs(nxt)

def bfs(start):
    queue=deque([start])
    visit[start]=True

    while queue:
        now=queue.popleft()

        for nxt in graph[now]:
            if visit[nxt]==False:
                visit[nxt]=True
                queue.append(nxt)


for i in range(1,n+1):
    if visit[i]==False:
        bfs(i)
        count+=1
print(count)