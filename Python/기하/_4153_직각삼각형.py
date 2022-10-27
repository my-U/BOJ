while True:
    L = list(map(int, input().split()))
    if L[0] == 0 and L[1] == 0 and L[2] == 0:
        break
    else:
        L.sort()
        if L[0] ** 2 + L[1] ** 2 == L[2] ** 2:
            print("right")
        else: print("wrong")