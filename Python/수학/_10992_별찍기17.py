t = int(input())

for i in range(1, t+1):
    if(i==1 or i==t):
        print(' ' * (t-i) + '*' * (2*i-1))
    else:
        print(' ' * (t-i) + '*' + ' ' * (2*i-3) + '*')