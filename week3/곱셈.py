x,y,z=map(int,input().split())

def pow(a,b,c):
    if b==1:
        return a%c

    half=pow(a,b//2,c)

    if b%2==0:
        return(half*half)%c
    else:
        return(a*half*half)%c
    
print((pow(x,y,z)))