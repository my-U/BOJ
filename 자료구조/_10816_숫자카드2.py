import sys
input = sys.stdin.readline

N = input().strip()
nCard = map(int, input().split())
M = input().strip()
mCard = map(int, input().split())
dict = {}

for i in nCard:
    if i in dict:
        dict[i] += 1 # 중복된 값이 존재할 경우 1 증가
    else:
        dict[i] = 1 # dict는 비어있기 때문에 새로이 추가될 때 1로 초기화

for j in mCard:
    if j in dict:
        print(dict[j], end=' ')
    else:
        print(0, end=' ')

# 참고 코드
# from collections import Counter 파이썬 내장모듈 Counter

# card = list(map(int, input().split()))
# test = list(map(int, input().split()))
# count = Counter(card) Counter에 리스트를 값으로 주면 해당 원소가 몇 개인지 세어서 dictionary 형태로 반환함

# for i in test:
#     if i in count:
#         print(count[i], end=' ')
#     else:
#         print(0, end=' ')

# 이 방법 외에 이진탐색으로 구현 가능
