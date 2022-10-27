A = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input()
cnt = 0
result = 0

for i in A:
    cnt += N.count(i)
result += (len(N) - len(i)*cnt) + cnt
print(result)

# 참고 코드
# for i in A:
#     N = N.replace(i, "0") N에서 모든 문자 i를 0으로 대체함
# print(len(N))