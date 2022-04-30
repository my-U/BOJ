import sys
from collections import Counter

N = int(sys.stdin.readline())
L = [0] * N

for i in range(N):
    L[i] = int(sys.stdin.readline())
L.sort()

count = Counter(L).most_common(2) # 여러개일 경우 두 번째로 작은 값을 출력하기 때문에 2개의 데이터만 가져옴

print(round(sum(L) / N)) # 산술평균
print(L[int(N / 2)]) # 중앙값
# 최빈값
if len(count) > 1: # 입력된 숫자가 1개 이상일 경우
    max_count = count[0][1] # 첫 번째 데이터 개수를 저장
    if count[0][1] == count[1][1]: # 만약 두 수의 개수가 같다면
        print(count[1][0]) # 두 번째로 작은 값 출력
    else:
        print(count[0][0]) # 첫 번째 값 출력
else:
    print(count[0][0]) # 입력된 숫자가 1개일 경우
print(max(L) - min(L)) # 범위