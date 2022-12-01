a = int(input())
b = int(input())
x = a
y = b
while x != 0 and y != 0:
    if x > y:
        x = x % y
    else:
        y = y % x
nod = int(x + y)
print(int(a * b / nod))
