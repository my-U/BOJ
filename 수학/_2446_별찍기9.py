t = int(input())

for i in range(t, 0, -1):
    print(' ' * (t-i) + '*' * (2*i-1))
for i in range(1, t):
    print(' ' * (t-i-1) + '*' * (2*i+1))