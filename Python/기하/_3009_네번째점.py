a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

if a == c:
    x = e
elif a == e:
    x = c
elif c == e:
    x = a

if b == d:
    y = f
elif b == f:
    y = d
elif d == f:
    y = b

print(x, y)

# 참조 코드
# def func(x, y, z): 
#  if x == y: return z
#  elif x == z: return y
#  else: return x

# print(func(a, c, e), func(b, d, f))