# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
n=int(input())
nums=sorted(map(int,input().split()))
m=int(input())
targets=list(map(int,input().split()))


'''
#for문은 시간초과
for target in targets: 
    if target in nums:
        print(1)
    else:
        print(0)
'''
def sol(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        elif nums[mid]==target:
            return print(1)
    return print(0)

for target in targets:
    sol(nums,target)