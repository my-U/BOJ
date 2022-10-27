N = int(input())
big = []

for _ in range(N):
    x, y = map(int, input().split())
    big.append((x, y))

for i in big: # 2차원 배열을 사용하지 않아도 됨
    rank = 1
    for j in big:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")

# 초기코드
# for i in range(N):
#     count = 1
#     for j in range(N):
#         if big[i][0] < big [j][0] and big[i][1] < big[j][1]:
#             count += 1
#     rank.append(count)
# print(rank)