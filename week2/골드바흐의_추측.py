def sol():
    def is_prime(p):
        if p<=1:
            return False
        if p==2:
            return True
        if p>=3:
            for i in range(2,int(p**(1/2))+1):
                if p%i==0:
                    break
            else:
                return True
    
    prime=[]
    for i in range(100):
        if is_prime(i)==True:
            prime.append(i)
    
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=n//2
        b=n//2

        while True:
            if is_prime(a) and is_prime(b):
                print(f"{a} {b}")
                break
            a-=1
            b+=1
sol()