from collections import deque
import sys
input=sys.stdin.readline

k=int(input())
for _ in range(k):
    v,e=map(int,input().split())
    graph=[[]for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    color=[0]*(v+1)
    is_bipartite=True

    for start in range(1,v+1):
        if color[start]!=0:
            continue
        queue=deque([start])
        color[start]=1

        while queue and is_bipartite:
            now=queue.popleft()

            for nxt in graph[now]:
                if color[nxt]==0:
                    color[nxt]=-color[now]
                    queue.append(nxt)
                elif color[nxt]==color[now]:
                    is_bipartite=False
                    break
        
    print("YES" if is_bipartite else "NO")