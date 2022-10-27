W, H, X, Y, P = map(int, input().split())
count = 0

for _ in range(P):
    x, y = map(int, input().split())
    r = H / 2
    disx1 = (X - x) ** 2
    disx2 = (X + W - x) ** 2
    disy = (Y + r - y) ** 2

    if X <= x <= X + W and Y <= y <= Y + H:
        count += 1
    elif disx1 + disy <= r ** 2 or disx2 + disy <= r ** 2:
        count += 1
print(count)