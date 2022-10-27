while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: # a와 b의 값이 0일 경우
        break # 실행 종료
    print(a+b)