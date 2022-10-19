while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    if x > y:
        result = x % y
        if result == 0:
            print("multiple")
        else:
            print("neither")
    else:
        result = y % x
        if result == 0:
            print("factor")
        else:
            print("neither")