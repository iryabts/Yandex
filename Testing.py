n = int(input())
m = 0
i = 2
answer = ""
while n // i > 0:
    for j in range(i, int(i ** 0.5) + 1):
        if i % j == 0:
            m += 1
    if m == 0 and n % i == 0:
        answer += f"{i}"
        n = n // i
    else:
        i += 1
print(answer)
