#recursion

def nsum(n):
    a=0
    for i in range(n+1):
        a+=i
        return a
    
    #return sum([i for i in range(n+1)])

#recursion : 함수를 정의할 때, 자기 자신을 또 후출하는 경우
#ex) sum(n)=n+sum(n-1)
def sum(n):
    return n+sum(n-1)
#위 처럼 정의하면 sum(-1),sum(-2)......끝도없다. base case를 정해야 함. RecursionError
# if n == 0:
#    return 0 
# else:
#    return n+sum(n-1)    을 추가해주면 됨

#tail recursion(return값이 다시 함수), 파이썬에선 그냥 포문을 써야함. 언어마다 다름
def sum_iter(n.total):
    if n==0:
        return total
    else:
        return sum_iter(n-1,total+n)

def sum(n):
    return sum_iter(n,0)


#거듭제곱
def exp(b,n):
    if n==0:
        return 1
    else:
        return b*exp(b,n-1)

#recursion 이 비효율적인 상황도 존재. 시간복잡도 공간복잡도 고려? 최적화 방법은?
def fast_exp(b,n):
    if n==0:
        return 1
    else:
        if n is even:
            return (b**(n/2))**2
        if n is odd:
            return b*fast_exp(b,n-1)

#피보나치를 구현하면 같은 값이 반복되어 복잡도가 올라감. tree구조.        
def fin(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1 :
        return fin(n-2)+fin(n-1)

# 재귀는 큰 문제를 작은 문제로 나누고, 그 작은 문제가 자기 자신과 구조가 동일할 때 적용할 수 있는 방법

