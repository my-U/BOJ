import sys
input = sys.stdin.readline # input보다 입출력방식이 더 빠르다

N = int(input())

for _ in range(N):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)