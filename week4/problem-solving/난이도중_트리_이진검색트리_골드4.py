# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
nums=[]
while True:
    try:
        nums.append(int(input()))
    except:
        break

def recursion(start,end):
    if start>end:
        return
    
    root=nums[start]
    mid=end+1

    for i in range(start+1,end+1):
        if nums[i]>root:
            mid=i
            break

    recursion(start+1,mid-1)
    recursion(mid,end)
    print(root)

recursion(0,len(nums)-1)