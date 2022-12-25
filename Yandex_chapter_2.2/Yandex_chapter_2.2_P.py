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
    print(f"{Pete_1:^24}\n{Vasya_1:>6}\n{Tolya_1:>22}\n{second:>5}{first:>7}{third:>9}")
elif Pete >= Tolya >= Vasya:
    print(f"{Pete_1:^24}\n{Tolya_1:>6}\n{Vasya_1:>22}\n{second:>5}{first:>7}{third:>9}")
elif Vasya >= Pete >= Tolya:
    print(f"{Vasya_1:^24}\n{Pete_1:>6}\n{Tolya_1:>22}\n{second:>5}{first:>7}{third:>9}")
elif Vasya >= Tolya >= Pete:
    print(f"{Vasya_1:^24}\n{Tolya_1:>6}\n{Pete_1:>22}\n{second:>5}{first:>7}{third:>9}")
elif Tolya >= Vasya >= Pete:
    print(f"{Tolya_1:^24}\n{Vasya_1:>6}\n{Pete_1:>22}\n{second:>5}{first:>7}{third:>9}")
elif Tolya >= Pete >= Vasya:
    print(f"{Tolya_1:^24}\n{Pete_1:>6}\n{Vasya_1:>22}\n{second:>5}{first:>7}{third:>9}")
