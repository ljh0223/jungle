v,e,start=map(int,input().split())
graph=[[]for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=set()
order=[]

def dfs(start):
    visited.add(start)
    order.append(start)
    
    for nxt in graph[start]:
        if nxt not in visited:
            dfs(nxt)
            print(*order)
    
dfs(start)