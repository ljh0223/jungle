# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque

def sol():

    n=int(input())
    queue=deque(i+1 for i in range(n))
    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue[0])

sol()