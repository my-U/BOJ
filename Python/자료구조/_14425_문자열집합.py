import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = {}
L = []
cnt = 0

for i in range(1, N+1):
    S[input().strip()] = i
for i in range(M):
    W = input().strip()
    if W in S:
        cnt += 1
print(cnt)
