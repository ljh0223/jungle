n,m=map(int,input().split())

stones=sorted(int(input()) for _ in range(m))

# def recursion(current=1,jump=1,count=0):
#     next=current+jump
#     if next==n:
#         return count+1

#     if next in stones:
#         count+=1
#         recursion(next-1,jump,count)
#     else:
#         jump+=1
#         count+=1
#         recursion(next,jump,count)

# print(recursion(1,1,0)) 실패

dp=[[11111]*(n+1) for _ in range(n+1)]
dp[1][0]=0
dp[1][1]=0
for i in range(1,n+1):
    if i in stones:
        continue
    for j in range(1,n+1):
        if dp[i][j]==11111:
            continue
        for nj in (j-1,j,j+1):
            if nj<1:
                continue
            next=i+nj
            if next>n:
                continue
            if next in stones:
                continue
            dp[next][nj]=min(dp[next][nj],dp[i][j]+1)

print(min(dp[n]))