n = int(input())
dig_1 = n // 100
dig_2 = n // 10 % 10
dig_3 = n % 10
dig_min = min(dig_1, dig_2, dig_3)
dig_max = max(dig_1, dig_2, dig_3)
if dig_min < dig_1 <= dig_max:
    dig_mid = dig_1
elif dig_min < dig_2 <= dig_max:
    dig_mid = dig_2
else:
    dig_mid = dig_3
print(dig_min, dig_mid, dig_max)
if dig_min == 0 and dig_max != 0 and dig_mid != 0:
    print(dig_mid, dig_min, " ", dig_max, dig_mid, sep="")
elif dig_min == 0 and dig_mid == 0 and dig_max != 0:
    print(dig_max, dig_min, " ", dig_max, dig_mid, sep="")
else:
    print(dig_min, dig_mid, " ", dig_max, dig_mid, sep="")
