import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

N = A*B*C
dp = list(str(N)) # list(str())은 문자열을 각각 요소로 나누어 리스트로 변환한다

for i in range(10):
    print(dp.count(str(i))) # array.count()는 해당 문자가 배열에 몇개 있는지 구해준다

# 참고 코드
# for j in range(10):
#     print(str(N).count(str(j))) # 리스트가 아닌 문자열에서도 count 가능