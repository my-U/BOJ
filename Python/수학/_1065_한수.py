H = int(input())
count = 0

for i in range(1, H+1):
    # 1자리수는 비교할 수들이 없어 한수
    # 2자리수는 공차가 1개이기 때문에 한수
    if i <= 99: 
        count += 1
    else:
        # 첫 번째 자릿수를 기준으로 나머지 자리를 구해야 된다 생각했는데
        # 각 자릿수들간의 차이가 같으면 됨
        N = list(map(int, str(i)))  
        # i // 100 - (i % 100) // 10 == (i % 100) // 10 - i % 10 리스트를 사용하지 않아도 됨
        if (N[0] - N[1]) == (N[1] - N[2]):  
            count += 1
        else:
            continue
print(count)
