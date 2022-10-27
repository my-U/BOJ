T= int(input()) # 반복할 횟수

for _ in range(T) : # 변수를 사용하지 않아도 될 시에는 _로 사용 가능, 0부터 T-1까지 반복
    a, b = map(int, input().split()) # 입력 받은 값을 정수로 변환하기 위해서 map을 사용하여 한 줄로 작성
    print(a+b)