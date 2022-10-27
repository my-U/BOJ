# 처음엔 리스트를 사용하지 않고 별을 하나씩 출력하는 방법으로 생각함
# 패턴을 나누는 방법과 지수를 구하는 방법 등 다양한 풀이의 고민이 필요함

def get_star(n):
    answer = []
    for i in range(len(n) * 3): # 줄 별 별의 개수가 3배씩 늘어나기 때문에 인자로 전달된 리스트의 길이 * 3만큼 i 반복. i를 각 줄들의 인덱스로 보면 됨
        if i // len(n) == 1: # len(n)이 3일 때, i가 3,4,5일 경우 
            answer.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else: # len(n)이 3일 때, i가 3, 4, 5가 아닐 경우
            answer.append(n[i % len(n)] * 3)
    return answer

star = ["***", "* *", "***"] # N이 3이었을 경우의 패턴을 줄별로 나눔
N = int(input())
count = 0

while N != 3: # N의 값이 3이 아닐 경우에만 실행
    count += 1 # N이 3보다 클 경우 재귀함수가 반복되는 횟수. N이 9일 경우 1번 반복, 27일 경우 2번 반복
    N = N // 3 # N이 3이 될 때까지 나누어 줌

for i in range(count):
    star = get_star(star) # get_star함수에 리스트 star을 넣어 실행한 후 나온 결과를 다시 star에 저장
for i in star:
    print(i)