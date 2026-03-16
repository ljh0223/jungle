# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
def sol():
    n=int(input())
    nums=sorted((int(input()) for _ in range(n)),reverse=True)
    '''시간초과 3중 for문
    new=nums[:-1]
    result=[]
    for num1 in new:
        for num2 in new:
            for num3 in new:
                if num1+num2+num3 in nums:
                    result.append(num1+num2+num3)

    print(max(result))
    '''
    sum2=set()
    for num1 in nums:
        for num2 in nums[:len(nums)-1]:
            sum2.add(num1+num2)
    for num1 in nums:
        for num2 in nums:
            if (num1-num2) in sum2:
                return print(num1)
sol()