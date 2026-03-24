from collections import deque
n=int(input())
m=int(input())

graph=[[] for i in range(n)]
for _ in range(m):
    x,y=map(int,input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

visited=[False]*n
visited[0]=True

queue=deque([0])

while queue:
    now=queue.popleft()


    for nxt in graph[now]:
        if visited[nxt]==False:
            visited[nxt]=True
            queue.append(nxt)

print(visited.count(True)-1)
