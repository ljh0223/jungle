from collections import deque
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[False]*(n+1)
visited[1]=True
parent=[0]*(n+1)

queue=deque([1])
while queue:
    now=queue.popleft()
    for nxt in graph[now]:
        if visited[nxt]==False:
            visited[nxt]=True
            parent[nxt]=now
            queue.append(nxt)

for i in range(2,n+1):
    print(parent[i])