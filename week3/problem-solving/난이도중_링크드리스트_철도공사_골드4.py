# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


n, m = map(int, input().split())
nums = list(map(int, input().split()))

nodes = {}

first = None
prev_node = None

for num in nums:
    new_node = Node(num)
    nodes[num] = new_node

    if first is None:
        first = new_node
    else:
        prev_node.next = new_node
        new_node.prev = prev_node

    prev_node = new_node

prev_node.next = first
first.prev = prev_node

answer = []

for _ in range(m):
    command = input().split()
    cmd = command[0]
    i = int(command[1])

    target = nodes[i]

    if cmd == 'BN':
        j = int(command[2])
        next_node = target.next
        answer.append(str(next_node.value))

        new_node = Node(j)
        nodes[j] = new_node

        target.next = new_node
        new_node.prev = target
        new_node.next = next_node
        next_node.prev = new_node

    elif cmd == 'BP':
        j = int(command[2])
        prev_station = target.prev
        answer.append(str(prev_station.value))

        new_node = Node(j)
        nodes[j] = new_node

        prev_station.next = new_node
        new_node.prev = prev_station
        new_node.next = target
        target.prev = new_node

    elif cmd == 'CN':
        delete_node = target.next
        answer.append(str(delete_node.value))

        next_node = delete_node.next
        target.next = next_node
        next_node.prev = target

    elif cmd == 'CP':
        delete_node = target.prev
        answer.append(str(delete_node.value))

        prev_station = delete_node.prev
        prev_station.next = target
        target.prev = prev_station

print('\n'.join(answer))