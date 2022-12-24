n = int(input())
d_1 = str(n // 1000)
d_2 = str(n // 100 % 10)
d_3 = str(n // 10 % 10)
d_4 = str(n % 10)
m = str(d_4 + d_3 + d_2 + d_1)
if str(n) == m:
    print("YES")
else:
    print("NO")
