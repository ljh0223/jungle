# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
n=int(input())

def f(n):
    if n<=1:
        return n
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b

print(f(n))