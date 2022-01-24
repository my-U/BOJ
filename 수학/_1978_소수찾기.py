N = int(input())
S = map(int, input().split())
count = 0

for num in S:
    E = 0
    if num > 1:
        for i in range(2, num): # num을 나눌 수 2부터 num-1까지
            if num % i == 0: # i로 나누어지면 소수가 아님
                E += 1
        if E == 0: # E가 0일 경우 나뉘어지는 수가 없으므로 소수
            count += 1
print(count)