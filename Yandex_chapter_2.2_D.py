Pete = int(input())
Vasya = int(input())
Tolya = int(input())
if Pete >= Vasya >= Tolya:
    print("1. Петя\n2. Вася\n3. Толя")
elif Pete >= Tolya >= Vasya:
    print("1. Петя\n2. Толя\n3. Вася")
elif Vasya >= Pete >= Tolya:
    print("1. Вася\n2. Петя\n3. Толя")
elif Vasya >= Tolya >= Pete:
    print("1. Вася\n2. Толя\n3. Петя")
elif Tolya >= Vasya >= Pete:
    print("1. Толя\n2. Вася\n3. Петя")
elif Tolya >= Pete >= Vasya:
    print("1. Толя\n2. Петя\n3. Вася")
