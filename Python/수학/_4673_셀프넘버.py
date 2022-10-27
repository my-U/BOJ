# 셀프 넘버는 생성자가 없기 때문에 계산으로는 구할 수 없다
# 때문에 1부터 10000까지의 수에서 생성자가 존재하는 수들을 제외하는 방법으로 구해야 한다
# 이를 구하기 위해서 집합 자료형인 set() 함수를 사용하여 차집합을 구한다

A = set(range(1, 10001))
N = set()

for i in A:
    # 정수인 i를 set을 사용하여 각 자릿수를 나누려고 했으나 i가 9965일 경우 9, 6, 5만 더해지는 경우가 생김
    for j in str(i): # 배열을 범위로 했을 때 j가 각 요소를 갖는 것 처럼 문자열도 j가 각 문자를 가짐
        i += int(j)
    N.add(i)
SelfNumber = sorted(A - N)
for i in SelfNumber:
    print(i)


# 참고 코드
# import sys

# def d(n: int):  d(n)을 구하는 함수 정의
#     return n + n//1000 + (n%1000)//100 + (n%100)//10 + n%10

# dList = [0]*10000
# for n in range(10000):
#     try:
#         dList[d(n)] = 1  만약 n이 1일 때 d(n) = 2, dList[2]는 1로 생성자가 있음을 의미함
#     except IndexError:
#         continue

# for d in range(10000):
#     if dList[d]==0:  dList[d]가 0일 경우 == 생성자가 없는 수들
#         print(d)