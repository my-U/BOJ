# 브루트포스는 모든 경우의 수를 고려해야 하는 것을 잊지말자

N = int(input())

for i in range(1, N + 1):
    num = sum(map(int, str(i))) # i의 각 자릿수 합을 구함
    M = i + num
    if M == N:
        print(i)
        break
    if i == N:
        print(0)
