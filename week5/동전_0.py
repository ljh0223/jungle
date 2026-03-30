n,k=map(int,input().split())

coins=[int(input()) for _ in range(n)]
coins.reverse()
count=0
for coin in coins:
    if coin>k:
        continue
    else:
        count+=k//coin
        k%=coin
print(count)