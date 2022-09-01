import sys

N = int(sys.stdin.readline()) # sys.stdin.readline으로 입력받을 경우 입력된 값 뒤에 줄바꿈이 입력되어 strip으로 제거해야 함
L = []

for i in range(N):
    L.append(sys.stdin.readline().strip())
set_L = set(L) # 중복 단어 삭제
L = list(set_L) # set 자료형은 순서가 없기 때문에 list로 변환을 해야함 
L.sort() # 알파벳 순으로 먼저 정렬한 후
L.sort(key=len) # 길이에 따라 정렬

for i in L:
    print(i)
