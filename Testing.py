n = int(input())
m = 0
p = int(n ** 0.5)
for i in range(2, p + 1):
    if n % i == 0:
        m += 1
if m == 0 and n != 1:
    print("YES")
else:
    print("NO")
