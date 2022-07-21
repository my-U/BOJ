import sys
N = str(sys.stdin.readline()).strip() # 문자열 마지막에 계속 \n이 들어가서 문자열에서 \n을 제거하는 strip()함수 사용
L = []

for i in N:
    L.append(int(i))

L = sorted(L, reverse=True)
for i in L:
    print(i, end='')

# 참고 코드
# N = int(input()) int로 받은 후에
# L = []
# for i in str(N): str로 변경 후 분해 가능
#     L.append(int(i))

