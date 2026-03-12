# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

from itertools import permutations

def sol():
    n=int(input())
    result=[]
    nums=list(map(int, input().split()))
    if n==0: return 0

    for p in permutations(nums):
        b=0
        for i in range(len(p)-1):
            a=p[i]-p[i+1]
            b+=abs(a)
        result.append(b)

    print(max(result))

sol()
