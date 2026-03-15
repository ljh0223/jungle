# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
def sol():

    left=list(input().strip())
    right=[]
    n=int(input())

    for _ in range(n):
        a=input().split()
        if a[0]=="B" and left:
            left.pop()
        elif a[0]=="L" and left:
            right.append(left.pop())
        elif a[0]=="D" and right:
            left.append(right.pop())
        elif a[0]=="P":
            left.append(a[1])
    return print("".join(left+right[::-1]))
sol()