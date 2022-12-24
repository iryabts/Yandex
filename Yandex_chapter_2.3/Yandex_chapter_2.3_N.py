n = int(input())
m = 0
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        m += 1
    elif n % i != 0:
        c += 1
if m == 2 and c == n - 2:
    print("YES")
else:
    print("NO")
