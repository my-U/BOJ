K = int(input())
L = []
width = 0; w_idx = 0 # width : 가장 긴 가로 길이, w_idx : 가장 긴 가로의 인덱스
height = 0; h_idx = 0

for i in range(6):
    x, y = map(int, input().split())
    L.append((x, y))
    if x == 1 or x == 2: # 방향이 동쪽, 서쪽일 경우
        if y > width:
            width = y
            w_idx = i
    if x == 3 or x == 4: # 방향이 남쪽, 북쪽일 경우
        if y > height:
            height = y
            h_idx = i

idx_list = [L[h_idx - 1], L[(h_idx + 1) % 6], L[w_idx - 1], L[(w_idx + 1) % 6]] 
# 가장 긴 두 변과 인접한 변 각각 2개씩을 저장함
# + 1을 했을 경우 리스트의 크기보다 커졌을 경우가 있을 수 있어 % 6의 나머지로 구해준다

S_square = 1
for i in L: # 입력받은 변들 중에
    if i not in idx_list: # 리스트에 저장된 변 4개 중 없다면 작은 사각형을 이루는 2개의 변의 길이이므로
        S_square *= i[1] # 각 변들을 곱해준다.

B_square = width * height
result = (B_square - S_square) * K
print(result)