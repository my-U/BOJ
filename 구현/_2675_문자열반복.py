N = int(input())

for i in range(N):
    R, S = input().split()
    P = ""
    for j in range(len(S)): # 참고 코드
        for k in range(int(R)):
            P += S[j]
    print(P)

# for i in S:
#     P += i * int(R) 각각의 문자를 반복하려는 횟수만큼 곱한다
# print(P)

# for ch in S:
#     print( ch*int(R), end='') P를 사용하지 않아도 가능
# print() 문자출력 이후 입력줄을 바꿔줌