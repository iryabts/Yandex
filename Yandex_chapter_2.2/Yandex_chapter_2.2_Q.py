a = float(input())
b = float(input())
c = float(input())
D = (b * b) - (4 * a * c)
if a == b == c == 0:
    print("Infinite solutions")
elif a == b == 0 and c != 0:
    print("No solution")
elif a == c == 0 and b != 0:
    x = 0
    print(f"{x:.2f}")
elif a == 0 and b != 0 and c != 0:
    x = -c / b
    print(f"{x:.2f}")
elif a != 0 and b == 0 and c == 0:
    x = 0
    print(f"{x:.2f}")
elif a != 0 and b == 0 and c != 0 and -c / a > 0:
    x_1 = (-c / a) ** 0.5
    x_2 = -(-c / a) ** 0.5
    min_s = min(x_1, x_2)
    max_s = max(x_1, x_2)
    print(f"{min_s:.2f} {max_s:.2f}")
elif a != 0 and b == 0 and c != 0 and -c / a < 0:
    print("No solution")
elif a != 0 and b != 0 and c == 0:
    x_1 = 0
    x_2 = -b / a
    min_s = min(x_1, x_2)
    max_s = max(x_1, x_2)
    print(f"{min_s:.2f} {max_s:.2f}")
elif a != 0 and b != 0 and c != 0 and D < 0:
    print("No solution")
elif a != 0 and b != 0 and c != 0 and D == 0:
    x = -b / 2 * a
    print(f"{x:.2f}")
elif a != 0 and b != 0 and c != 0 and D > 0:
    x_1 = (-b + (D ** 0.5)) / (2 * a)
    x_2 = (-b - (D ** 0.5)) / (2 * a)
    max_s = max(x_1, x_2)
    min_s = min(x_1, x_2)
    print(f"{min_s:.2f} {max_s:.2f}")
