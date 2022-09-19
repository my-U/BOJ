import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
M = int(input())
P = list(map(int, input().split()))

dict = {}
for i in L:
    dict[i] = 1

for i in P:
    if i in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')

# 처음엔 list L과 P로만 포함되는지 찾으려고 했는데
# 계속 시간초과가 뜸
# 검색해본 결과 dictionary가 탐색 속도가 훨씬 빠르다는 것을 알게됨
# list는 자료 크기에 비례하여 시간이 늘어나지만
# dictionary는 거의 일정한 시간으로 탐색을 완료함