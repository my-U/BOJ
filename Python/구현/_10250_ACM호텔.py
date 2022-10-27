T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    Y = N % H
    X = N // H
    if Y == 0:
        print(100*H + X)
    else:
        print(100*Y + X + 1)