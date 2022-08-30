import sys

N = int(sys.stdin.readline())
L = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    L.append((x, y))
# L.sort(key=lambda x:x[0]) L[x][0]을 기준으로 정렬함 
b = sorted(L)
for i in b:
    print(i[0], i[1])