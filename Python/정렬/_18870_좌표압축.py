import sys
input = sys.stdin.readline

N = int(input())
dict = {} # 대응관계를 나타낼 수 있는 자료형 예) 이름 = 홍길동, 생일 = 1월 1일

num = list(map(int, input().split()))
set_num = sorted(set(num)) # 중복이 있다면 값이 증가하기 때문에 중복된 숫자 제거

for i in range(len(set_num)):
    dict[set_num[i]] = i # key에 대응하는 value 부여

for i in num:
    print(dict[i], end=' ')