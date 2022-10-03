# 교집합 문제

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
L1 = set()
L2 = set()

for i in range(N):
    L1.add(input().strip())
for i in range(M):
    L2.add(input().strip())

result = sorted(list(L1 & L2)) # 교집합

print(len(result))
for i in result:
    print(i)