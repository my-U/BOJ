N = int(input())
num = 666
cnt = 0

while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1 # num을 1씩 증가시키면서 666이 들어가는 모든 숫자를 검사하여 cnt와 N이 일치할 경우 num 출력