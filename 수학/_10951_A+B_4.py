while True:
    try: # 오류가 발생할 수 있는 코드
        a, b = map(int, input().split())
        print(a+b)
    except: # 오류가 발생했을 때 처리 코드
        break