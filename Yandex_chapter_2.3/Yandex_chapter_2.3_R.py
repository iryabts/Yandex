n = int(input())
m = 0
answer = str()
for i in range(2, n + 1):
    if n // i != 0:
        print(i)
        for j in range(2, int((i ** 0.5)) + 1):
            if i % j == 0:
                m += 1
                if m == 0:
                    answer = str(i)
    n = n // i
    print(n)
    if n == 0:
        break
answer += f" * {answer}"
print(answer)
