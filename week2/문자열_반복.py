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

