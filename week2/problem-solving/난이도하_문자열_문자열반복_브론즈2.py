# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
S="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$%*+-./:"
T=int(input())
for _ in range(T):
    R,t=input().split()
    R=int(R)
    result=""
    for alpha in t:
        ind=S.index(alpha)
        result+=R*S[ind]
    print(result)

