import sys
input=sys.stdin.readline

n,m=map(int,input().split())
nums=[list(map(int,input().split())) for _ in range(n)]

dp=[[0]*n for _ in range(n)] #dp[i][j]는 nums의 i행 리스트[j:]의 합

for i in range(n):
    for j in range(n):
        dp[i][j]=sum(nums[i][j:])

# print(dp)
for _ in range(m):
    a,b,c,d=map(int,input().split())
    # print(a,b,c,d)
    count=0
    if (a,b)!=(c,d):
        for i in range(a-1,c):
            count+=dp[i][b-1]
            if d<n:
                count-=dp[i][d]
        print(count)
    else:
        print(nums[a-1][b-1])


# n,m=map(int,input().split())
# nums=[list(map(int,input().split())) for _ in range(n)]

# dp=[[0]*n for _ in range(n)] #dp[i][j]는 nums의 i행 리스트[j:]의 합

