W = input()
E = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in E:
    if i in W:
        print(W.index(i), end=" ")
    else:
        print(-1, end=" ")

# E = "abcdefghijklmnopqrstuvwxyz" 배열이 아닌 문자열로도 가능
# E = map(chr, range(97, 123)) 아스키코드 97번부터 122번까지를 문자로 변환