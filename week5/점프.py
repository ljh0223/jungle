n,m=map(int,input().split())
stones=[int(input()) for _ in range(m)]

dp=[[10000]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    if i not in stones:
        dp[i][1]=i-1

    for j in range(1,n+1):
        if i in stones:
            continue
        if i-j<1:
            continue
        dp[i][j]=min(dp[i-j][j],dp[i-j][j-1],dp[i-j][j+1])+1

print(min(dp[n]))