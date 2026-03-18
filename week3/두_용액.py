n=int(input())
liquid=sorted(map(int,input().split()))
mixed=[]
def sol():
    left=0
    right=len(liquid)-1
    min_mix=float('inf')
    answer_left=0
    answer_right=0

    while left<right:
        mix=liquid[left]+liquid[right]
        if mix==0:
            return print(liquid[left],liquid[right])
        elif mix<0:
            if abs(mix)<min_mix:
                min_mix=abs(mix)
                answer_left=liquid[left]
                answer_right=liquid[right]
            left+=1
        else:
            if abs(mix)<min_mix:
                min_mix=abs(mix)
                answer_left=liquid[left]
                answer_right=liquid[right]
            right-=1
    return print(answer_left, answer_right)

sol()