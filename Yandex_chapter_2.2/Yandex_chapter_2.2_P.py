Pete = int(input())
Vasya = int(input())
Tolya = int(input())
Pete_1 = "Петя"
Vasya_1 = "Вася"
Tolya_1 = "Толя"
first = "I"
second = "II"
third = "III"
if Pete >= Vasya >= Tolya:
    print(f"{Pete_1:^24}\n{Vasya_1}\n{Tolya_1:>24}\n {second}{first:^17}{third}")
elif Pete >= Tolya >= Vasya:
    print(f"{Pete_1:^24}\n{Tolya_1}\n{Vasya_1:>24}\n {second}{first:^17}{third}")
elif Vasya >= Pete >= Tolya:
    print(f"{Vasya_1:^24}\n{Pete_1}\n{Tolya_1:>24}\n {second}{first:^17}{third}")
elif Vasya >= Tolya >= Pete:
    print(f"{Vasya_1:^24}\n{Tolya_1}\n{Pete_1:>24}\n {second}{first:^17}{third}")
elif Tolya >= Vasya >= Pete:
    print(f"{Tolya_1:^24}\n{Vasya_1}\n{Pete_1:>24}\n {second}{first:^17}{third}")
elif Tolya >= Pete >= Vasya:
    print(f"{Tolya_1:^24}\n{Pete_1}\n{Vasya_1:>24}\n {second}{first:^17}{third}")
