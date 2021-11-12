A = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
B = [ "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" ]

x, y = map(int, input().split())
Day = 0
for i in range(0, x-1):
    Day += A[i]

Day = (Day + y) % 7
print(B[Day])
