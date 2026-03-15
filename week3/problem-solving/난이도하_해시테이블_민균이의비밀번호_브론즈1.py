# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
N=int(input())

N=int(input())

def sol():
    pw_list=[]
    result=[]
    for _ in range(N):
        pw_list.append(input())
    for pw in pw_list:
        if pw[::-1] in pw_list:
            if not result:
                result.append(pw)

    return print(len(result[0]), result[0][len(result[0])//2] )



def sol2():
    pw_set=set()
    for _ in range(N):
        pw=input()
        if (pw[::-1] in pw_set) or pw==pw[::-1]:
            print(len(pw), pw[len(pw)//2])
        else:
            pw_set.add(pw)
sol2()