n = int(input())
m = 0
c = 0
for i in range(1, n + 1):
    while m < 3:
        if n % i == 0:
            m += 1
if m < 3:
    print("YES")
else:
    print("NO")
