N = int(input())
a = 1
sum = 1

while N > sum:
    a += 1
    sum += a

b = sum - N
if a%2 == 0:
    print(str(a-b) + '/' + str(1+b))
else:
    print(str(1+b) + '/' + str(a-b))

# 참고 코드
# k=int(input())
# n=1
# while n<k:
#     k=k-n  k가 n보다 작아졌을 때 k가 몇번째인지 알 수 있기 때문에 sum을 사용하지 않아도 됨
#     n+=1

# if n%2==0:
#     print('{}/{}'.format(k,n+1-k)) format을 사용하여 str으로 변환하지 않아도 됨
# else:
#     print('{}/{}'.format(n+1-k,k))