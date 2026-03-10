# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

import sys
# 로컬 PC(VS Code) 환경에서만 파일을 읽어오도록 설정
# 백준 서버에 제출할 때는 이 아랫부분은 지우거나 주석 처리해야 합니다.
sys.stdin = open("4344.txt", "r")

def solve():
    c = int(sys.stdin.readline())
    avg_list=[]
    n_list=[]
    for _ in range(c):
        data = list(map(int, sys.stdin.readline().split()))
        n = data[0]
        n_list.append(n)
        scores = data[1:]
        avg=sum(scores)/n
        avg_list.append(avg)
        count=0
        for s in scores:
            if s > avg:
                count+=1
    
        rate=(count/n)*100
        print(f"{rate:.3f}%")

solve()