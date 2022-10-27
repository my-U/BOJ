N = int(input())
X = list(map(int, input().split()))
sum = 0

for i in range(N):
    sum += (X[i]/max(X))*100 # X[i] = (X[i]/max(X))*100 sum을 사용하지 않아도 됨
print(sum/N)
