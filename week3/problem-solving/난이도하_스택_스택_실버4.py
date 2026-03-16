# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
n=int(input())
stack=[]

for m in range(n):
    m=input()
    if "push" in m:
        stack.append(int(m.split()[1]))
    elif m=="top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif m=="pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif m=="empty":
        if stack:
            print(0)
        else:
            print(1)
    elif m=="size":
        print(len(stack))

