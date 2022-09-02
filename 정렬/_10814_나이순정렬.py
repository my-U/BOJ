N = int(input())
L = []

for i in range(N):
    x, y = map(str, input().split())
    x = int(x) # 나이만 정수로 변경 후 리스트에 저장
    L.append((x, y))

L.sort(key = lambda x : x[0])

for i in L:
    print(i[0], i[1])