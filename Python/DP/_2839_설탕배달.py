N = int(input())
dp = 0

while N >= 0:
    if(N % 5 == 0):
        dp = dp + N // 5
        print(dp)
        break
    N -= 3 # 5의 배수가 아닐경우 3씩 감소 반복
    dp = dp + 1 # 3이 감소될 경우 1씩 증가 => 3키로 설탕봉지의 개수
else :
    print(-1) # 입력받은 값이 위의 코드에 해당하지 않을 경우 -1 출력