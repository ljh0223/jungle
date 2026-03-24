# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
from collections import deque

n,m=map(int,input().split())
board=[list(map(int,input().strip())) for _ in range(n)]
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
bfs를 사용해야 함
"""
def bfs(x,y,count=0):
    queue=deque([(0,0)])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if board[nx][ny]==1:
                    board[nx][ny]=board[x][y]+1
                    queue.append((nx,ny))
    return board[n-1][m-1]

print(bfs(0,0,0))