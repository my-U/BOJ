S = input()
L = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        L.add(S[i:j+1]) # 부분문자열 구하기
print(len(L))
