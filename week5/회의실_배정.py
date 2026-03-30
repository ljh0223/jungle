import sys
input=sys.stdin.readline

n=int(input())
meetings=[tuple(map(int,input().split())) for _ in range(n)]
new_m=[]
for x,y in meetings:
    new_m.append((y,x))
new_m.sort()

current=new_m[0][0]
count=1

for meeting in new_m[1:]:
    if meeting[1]>=current:
        current=meeting[0]
        count+=1

print(count)