n = input()
z = len(n)
n = int(n)
text = ""
for i in range(1, z + 1):
    m = n % 10
    n = n // 10
    if m % 2 != 0:
        text = text + str(m)
print(text[::-1])
