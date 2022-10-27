N, M = map(int, input().split())
chess = []
result = []

for _ in range(N):
    chess.append(input())

for i in range(N - 7): # 8개씩 잘랐을 때 반복되는 횟수 = (N - 8) + 1
    for j in range(M - 7):
        first_W = 0 # 첫 번째 정사각형이 흰색으로 칠해졌을 때 다시 칠해지는 정사각형의 개수
        first_B = 0 # 첫 번째 정사각형이 검정색으로 칠해졌을 때 다시 칠해지는 정사각형의 개수
        # 8*8 보드를 한 칸씩 검사하기
        for p in range(i, i + 8):
            for q in range(j, j + 8):
                if (p + q) % 2 == 0: # 첫 번째 정사각형과 칠해지는 색이 같다
                    if chess[p][q] != 'W': # 흰색이 아닐 경우 흰색으로 다시 색칠하기 때문에 first_W의 값 1증가
                        first_W += 1
                    if chess[p][q] != 'B': # 검정색이 아닐 경우 검정색으로 다시 색칠하기 때문에 first_B의 값 1증가
                        first_B += 1
                else:
                    if chess[p][q] != 'W': # 첫 번째가 검정색일 때 p + q가 홀수면 해당 정사각형은 흰색이어야 함. 만약 흰색이 아니라면 흰색으로 다시 색칠해야 하므로 first_B의 값이 1증가
                        first_B += 1
                    if chess[p][q] != 'B':
                        first_W += 1
        result.append(first_W)
        result.append(first_B)
print(min(result))