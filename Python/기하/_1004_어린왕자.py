T = int(input())

for _ in range(T):
    count = 0   
    x1,y1,x2,y2 = map(int,input().split())
    N = int(input())
    
    for _ in range(N):
        cx,cy,r = map(int,input().split())
        dis1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        dis2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        pow_r = r ** 2
        if dis1 < pow_r and dis2 < pow_r:
            continue
        elif pow_r > dis1 or pow_r > dis2:
            count +=1

    print(count)