n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
y = (n * k1 - n * m) / (k1 - k2)
x = n - y
print(int(x), int(y))
