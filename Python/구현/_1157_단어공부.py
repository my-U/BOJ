A = input().upper()
set_A = list(set(A))
cnt_list = []

for i in set_A:
    cnt = A.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1: # 가장 큰 수가 2개 이상일 경우
    print("?")
else:
    print(set_A[cnt_list.index(max(cnt_list))]) # 가장 큰 수의 인덱스를 구함