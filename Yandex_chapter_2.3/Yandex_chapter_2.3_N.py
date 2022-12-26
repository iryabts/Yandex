n = int(input())
m = 0
p = int(n ** 0.5)
for i in range(1, p):
    if n % i == 0:
        m += 1
        if m > 2:
            break
if m == 2:
    print("YES")
else:
    print("NO")
