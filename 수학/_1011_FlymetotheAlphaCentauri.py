T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    distance = Y - X
    count = 0 # 이동 횟수
    move = 1 # count별 빈도수
    sum = 0

    while sum < distance:
        count += 1
        sum += move # move의 합인 sum이 count만큼 이동 가능한 최대의 distance
        if count % 2 == 0: # count가 짝수일 경우 다음 move의 값이 1증가함
            move += 1
    print(count)