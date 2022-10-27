import sys

input = sys.stdin.readline

A, B = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = a ^ b # 대칭차집합 = 교차하는 원소를 제외한 집합
print(len(result))