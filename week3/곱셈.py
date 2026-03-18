nums=list(map(int,input().split()))
a=nums[0]
b=nums[1]
c=nums[2]

def pow(x,y,z):
    return (x**y)%z

def half(x,y,z):
    if y%2 != 0:
        y=1+(y//2)**2
    else:
        y=P