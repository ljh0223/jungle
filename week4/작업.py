from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]

def topological(data):
    graph=[[] for _ in range(n+1)]
    indegree=[0]*(n+1)
    time=[0]*(n+1)
    result=[0]*(n+1)

    for i, work in enumerate(data):
        current = i+1
        time[current]=work[0]
        indegree[current]=work[1]

        for pre in work[2:]:
            graph[pre].append(current)
    
    queue=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
            result[i]=time[i]
    
    while queue:
        x=queue.popleft()
        for nxt in graph[x]:
            indegree[nxt]-=1
            result[nxt]=max(result[nxt],result[x]+time[nxt])

            if indegree[nxt]==0:
                queue.append(nxt)
            
    return max(result)

print(topological(data))
