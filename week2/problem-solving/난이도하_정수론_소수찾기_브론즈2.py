# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
n=input()
data=list(map(int, input().split()))

def sol():
    prime=[]
    for i in data:
        if i<2:
            continue
        elif i==2:
            prime.append(i)
        else:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                   break
            else:
                prime.append(i)

    return len(prime)
print(sol())