# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562


#테스트용
test_data=[3,29,38,12,57,74,40,85,61]

number = []
for num in test_data:
    number.append(num)

m=max(number)
print (m, number.index(m)+1)



#제출용
number = []
for _ in range(9):
    number.append(int(input()))

m=max(number)
print (m, number.index(m)+1)