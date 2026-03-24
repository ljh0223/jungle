"""
from collections import deque

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

queue=deque([(0,0)])
visited[0][0]=True

while queue:
    x,y=queue.popleft()
    if x==n-1 and y==n-1:
        print("HaruHaru")
        break
    
    jump=board[x][y]
    nx,ny=x+jump,y
    if nx<n and not visited[nx][ny]:
        visited[nx][ny]=True
        queue.append((nx,ny))
    
    nx,ny=x,y+jump
    if ny<n and not visited[nx][ny]:
        visited[nx][ny]=True
        queue.append((nx,ny))

else:
    print("Hing")
"""

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
visited[0][0]=True
def recursion(x,y):
    jump=board[x][y]
    if x==n-1 and y==n-1:
        visited[n-1][n-1]=True
        return print("HaruHaru")
    
    if x+jump<n:
        recursion(x+jump,y)
        visited[x+jump][y]=True
    if y+jump<n:
        recursion(x,y+jump)
        visited[x][y+jump]


recursion(0,0)
if visited[n-1][n-1]==False:
    print("Hing")