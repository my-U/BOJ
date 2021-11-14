t = int(input())

for i in range(t, 0, -1):
    print(' ' * (t-i) + '*' * (2*i - 1))