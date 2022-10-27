N = int(input())
sum = 0

A = list(map(int, input()))
for i in A:
    sum += i
print(sum)

# 참고 코드
# A = list(map(int, input()))  or  A = map(int, input())
# print(sum(A)) 각 요소를 더하지 않아도 sum()함수로 한번에 더할 수 있음