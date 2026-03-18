def sol():
    s=int(input())
    nums=[list(map(int,input().split())) for _ in range(s)]
    white_count=0
    blue_count=0

    def cut(x,y,s):
        nonlocal white_count, blue_count
        sum_num=sum(sum(row[y:y+s]) for row in nums[x:x+s])
        if sum_num==0:
            white_count+=1
            return
        elif sum_num==s**2:
            blue_count+=1
            return     
        half=s//2
        cut(x,y,half)
        cut(x,y+half,half)
        cut(x+half,y,half)
        cut(x+half,y+half,half)

    cut(0,0,s)
    return print(white_count), print(blue_count)

sol()