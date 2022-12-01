n = int(input())
m = n % 10
while n > 0:
    n = n // 10
    m = m + n % 10
print(m)
