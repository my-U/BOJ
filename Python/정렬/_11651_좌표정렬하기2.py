import sys

N = int(sys.stdin.readline())
L = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    L.append((x, y))

L.sort(key = lambda x : (x[1], x[0])) 
# 정렬 기준은 요소x의 1번 인덱스에 대해서 먼저 오름차순으로 정렬한 뒤, 동일한 값일 경우 0번째 인덱스에 대해서 오름차순으로 정렬된다.

for i in L:
    print(i[0], i[1])