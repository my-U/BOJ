N = int(input())

start_num = 1
cnt = 1

while N > start_num:
    start_num += 6 * cnt # 벌집이 6의 배수로 증가
    cnt += 1 # 이동하는 방의 수 증가
print(cnt)