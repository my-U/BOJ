dp = [0]

for _ in range(9):
    dp.append(int(input())) 

print(max(dp))
print(dp.index(max(dp)))

# 참고 코드
# dp = [int(input()) for i in range(9)] 더욱 간결해짐