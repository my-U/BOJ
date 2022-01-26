M = int(input())
N = int(input())
L = []

for i in range(M, N+1):
    S = 0
    if i > 1:
        for j in range(2, i): # i가 2일 경우 범위가 2에서 2이므로 성립이 되지 않아 S = 0이다
            if i % j ==  0:
                S += 1
        if S == 0:
            L.append(i)

if sum(L) == 0:
    print(-1)
else:
    print(sum(L))
    print(min(L))