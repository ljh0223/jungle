from collections import deque

n,m=map(int,input().split())
before=[]
after=[]

for _ in range(n):
    x,y=map(int,input().split())
    before.append(x)
    after.append(y)
for _ in range(m):
    x,y=map(int,input().split())
    before.append(x)
    after.append(y)

def bfs():
        
    dx=[1,2,3,4,5,6]
    queue=deque([1])
    visited=[False]*101
    visited[1]=True
    count=0
    while queue:
        size=len(queue)
        for _ in range(size):
            now=queue.popleft()
            for i in range(6):
                nx=now+dx[i]
                for j in range(len(before)):
                    if nx == before[j]:
                        nx=after[j]
                        break
                if nx==100:
                    return count+1
                elif nx<100 and visited[nx]==False:
                    visited[nx]=True
                    queue.append(nx)
        count+=1    

print(bfs())