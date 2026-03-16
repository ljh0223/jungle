# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
'''''''''
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
'''

import sys

input = sys.stdin.readline


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


text = input().rstrip()
m = int(input())

head = Node(None)
tail = Node(None)
head.next = tail
tail.prev = head

cursor = tail

for ch in text:
    new_node = Node(ch)
    left = cursor.prev

    left.next = new_node
    new_node.prev = left

    new_node.next = cursor
    cursor.prev = new_node

for _ in range(m):
    command = input().split()

    if command[0] == 'L':
        if cursor.prev != head:
            cursor = cursor.prev

    elif command[0] == 'D':
        if cursor != tail:
            cursor = cursor.next

    elif command[0] == 'B':
        if cursor.prev != head:
            target = cursor.prev
            left = target.prev

            left.next = cursor
            cursor.prev = left

    else:
        new_node = Node(command[1])
        left = cursor.prev

        left.next = new_node
        new_node.prev = left

        new_node.next = cursor
        cursor.prev = new_node

result = []
current = head.next

while current != tail:
    result.append(current.value)
    current = current.next

print(''.join(result))