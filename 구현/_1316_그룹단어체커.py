N = int(input())
cnt = 0

for _ in range(N):
    S = input()
    A = []
    for i in range(len(S)):
        if i == 0:
            A.append(S[i])
        else:
            if S[i] == S[i-1]:
                continue
            else:
                if A.count(S[i]) > 0:
                    cnt += 1
                    break
                else:
                    A.append(S[i])
print(N-cnt)

# 참고 코드
# if i != len(S) -1  i가 마지막 인덱스가 아닐 때
#     if S[i] == S[i+1]: 일치한다면 연속되므로 패스
#         pass
#     else S[i] in S[i+1:]: 일치하지 않았을 때 S[i+1]이후 S[i]가 있다면 연속되지 않으므로 break 
#         break

# 참고 코드
# S = input()
# if list(S) == sorted(S, key=S.find): 
#     cnt += 1
# key를 기준으로 S를 정렬한다
# 만약 S가 banana일 경우 S.find를 기준으로 정렬하면
# S.find('b')를 한 후 S에서 b를 정렬, S.find('a')를 한 후 S에서 a를 정렬, S.find('n')를 한 후 S에서 n을 정렬한 것으로
# 결과는 ['b', 'a', 'a', 'a', 'n', 'n']가 된다