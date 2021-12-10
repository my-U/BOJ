N = int(input())

for i in range(N):
    Q = list(map(str, input())) # Q = input() 가능. 문자 요소마다 나누지 않아도 인덱스 사용이 가능하기 때문

    for j in range(len(Q)):
        if j == 0:
            if Q[j] == 'O':
                S = [1]
            else:
                S = [0]
        else:
            if Q[j] == 'O':
                S.append(S[j-1] + 1)
            else:
                S.append(0)

    print(sum(S))

# 참고 코드
# for i in range(a):
#     b=sys.stdin.readline() 
#     n=0
#     score=0
#     for j in range(len(b)):
#         if(b[j]=='O'): 문자열은 list가 아니라도 인덱스 사용 가능
#             n+=1
#             score+=n  O일 경우 1씩 증가하고 증가한 값을 더해감
#         elif(b[j]=='X'):
#             n=0
#     print(score)
