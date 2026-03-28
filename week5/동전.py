T=int(input())
for _ in range(T):
    n=int(input())
    coins=list(map(int,input().split()))
    total=int(input())
    dp=[0]*(total+1)
    dp[0]=1
    dp[coins[0]]=1
    for i in range(coins[0],coins[1]):
        if i%coins[0]==0:
            dp[i]=1
