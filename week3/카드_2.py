from collections import deque

def sol():

    n=int(input())
    queue=deque(i+1 for i in range(n))
    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue[0])

sol()