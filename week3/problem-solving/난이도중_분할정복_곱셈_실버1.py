# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

x,y,z=map(int,input().split())

def pow(a,b,c):
    if b==1:
        return a%c

    half=pow(a,b//2,c)

    if b%2==0:
        return(half*half)%c
    else:
        return(a*half*half)%c
    
print((pow(x,y,z)))