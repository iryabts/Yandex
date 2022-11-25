# while (a := float(input())) != 0:
#    print(round(a, 1))
#    print(round(a, 2))
#    print(round(a, 3))
n = int(input())
dig_1 = n // 100
dig_2 = n % 100 // 10
dig_3 = n % 10
print(dig_1, dig_2, dig_3)
