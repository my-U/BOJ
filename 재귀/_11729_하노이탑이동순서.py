# 원판이 2이상인 n개일 경우 n개의 원판을 첫 번째 장대에서 세 번째 장대로 옮기려면
# 가장 마지막에 있는 원판을 제외한 n-1개의 원판을 두 번째 장대로 옮기고
# 가장 마지막 원판을 세 번째 장대로 옮긴 후
# 두 번째 장대에 있던 n-1개의 원판을 세 번째 장대로 옮기면 된다


def hanoi(k, one, three):
    if k == 1:
        print(one, three)
        return
    else:
        # 1단계 : 마지막 원판을 제외한 k-1개의 원판을 첫 번째 장대에서 두 번째 장대로 옮긴다
        hanoi(k-1, one, 6 - one - three) # 세 장대의 합이 6이기 때문에 6에서 첫 번째와 세 번째 장대를 빼면 두 번째 장대값이 나온다
        # 2단계 : 마지막 원판을 세 번째 장대로 옮김
        print(one, three)
        # 3단계 : 두 번째 장대에 있는 k-1개의 원판을 세 번째 장대로 옮김
        hanoi(k-1, 6 - one - three, three)        

k = int(input())

print(pow(2, k) - 1)
hanoi(k, 1, 3)

