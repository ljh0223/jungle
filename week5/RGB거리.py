import sys
input=sys.stdin.readline

n=int(input())
costs=[tuple(map(int,input().split())) for _ in range(n)]

dp=[[0]*3 for _ in range(n)]

for i in range(3):
    dp[0][i]=costs[0][i]

for i in range(1,n):
    for j in range(3):
        dp[i][j]=min(dp[i-1][(j+1)%3]+costs[i][j],dp[i-1][(j+2)%3]+costs[i][j])
    
print(min(dp[n-1]))