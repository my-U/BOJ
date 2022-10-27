import sys
N = int(input())
L = []

for i in range(N):
    L.append(int(sys.stdin.readline())) # input()을 사용했을 때 계속 시간초과가 나와서 sys를 사용하여 시간초과 해결

# L.sort()
# list의 경우 list.sort()는 복사본을 만들 필요가 없기 때문에 sorted()보다 빠르다 
for i in sorted(L):
    print(i)