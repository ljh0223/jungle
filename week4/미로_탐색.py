n,m=map(int,input().split())
board=[list(map(int,input().strip())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
"""
def dfs(x,y,count=0):
    visited[x][y]=True
    count+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]==1 and visited[nx][ny]==False:
                dfs(nx,ny,count)
    return count
            
dfs(0,0,0)
"""

queue=deque([start])