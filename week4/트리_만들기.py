n,m=map(int,input().split())

for i in range(n-m):
    print(i,i+1)

for j in range(n-m,n-1):
    print(n-m,j+1)