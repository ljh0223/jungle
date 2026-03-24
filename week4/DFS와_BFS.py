from collections import deque

v,e,start=map(int,input().split())
graph=[[]for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,v+1):
    graph[i].sort()
visited=set()
order=[]

def dfs(start):
    visited.add(start)
    order.append(start)
    
    for nxt in graph[start]:
        if nxt not in visited:
            dfs(nxt)
            
dfs(start)
print(*order)

def bfs():
    queue=deque([start])
    visited_que=set()
    visited_que.add(start)
    result=[start]

    while queue:
        now=queue.popleft()

        for nxt in graph[now]:
            if nxt not in visited_que:
                visited_que.add(nxt)
                result.append(nxt)
                queue.append(nxt)

    print(*result)

bfs()