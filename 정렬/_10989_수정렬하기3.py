import sys

N = int(sys.stdin.readline())
L = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline()) # 숫자를 입력할 때마다
    L[input_num] += 1 # 해당 인덱스의 값을 1씩 증가시킴

for i in range(10001):
    if L[i] != 0: # 값이 0이 아닐 경우
        for _ in range(L[i]): # 해당하는 값만큼 인덱스를 반복 출력
            print(i)