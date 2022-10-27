import sys
input = sys.stdin.readline

N, K = map(int, input().split())

L = list(map(int, input().split()))
L.sort(reverse=True)

print(L[K-1])

# 참고 코드
# L.sort() 오름차순으로 정렬 후
# print(L[-K]) 마지막 인덱스가 -1이므로 뒤에서 K번째 값 출력