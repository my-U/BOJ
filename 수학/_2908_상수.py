A, B = input().split()
A = int("".join(reversed(A))) # 반대로 뒤집은 후 join으로 연결
B = int("".join(reversed(B)))

print(A if A > B else B)

# 참고 코드
# x, y = input().split()
# print(max(int(x[::-1]), int(y[::-1])))  [::-1] -> 문자열이나 리스트 또는 튜플 등 역순으로 뒤집는다.