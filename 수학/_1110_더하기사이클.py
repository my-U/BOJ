import sys
input = sys.stdin.readline

N = int(input())
C = N
count = 0

while C >= 0:
    A = C // 10
    B = C % 10
    C = B*10 + (A+B)%10
    count += 1
    if C == N:
        break

print(count)