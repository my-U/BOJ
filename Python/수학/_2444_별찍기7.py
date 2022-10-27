t = int(input())

for i in range(1, t+1):
    print(' ' * (t-i) + '*' * (2*i -1))

for i in range(1, t):
    print(' ' * i + '*' * (2*(t-i) -1))
 