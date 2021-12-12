import sys
input = sys.stdin.readline

C = int(input())

for i in range(C):
    A = list(map(int, input().split()))
    count = 0
    
    avg = sum(A[1:])/A[0]
    for j in A[1:]:
        if j > avg:
            count += 1
    result = count/A[0] * 100
    print(f'{result:.3f}%')