n = int(input())
dig_1 = n // 100
dig_2 = n // 10 % 10
dig_3 = n % 10
dig_max = max(dig_1, dig_2, dig_3)
dig_min = min(dig_1, dig_2, dig_3)
dig_mid = dig_1 + dig_2 + dig_3 - dig_max - dig_min
if dig_min != 0 and dig_mid != 0 and dig_max != 0:
    print(f"{dig_min}{dig_mid} {dig_max}{dig_mid}")
elif dig_min == 0 and dig_mid != 0 and dig_max != 0:
    print(f"{dig_mid}{dig_min} {dig_max}{dig_mid}")
elif dig_min == 0 and dig_mid == 0 and dig_max != 0:
    print(f"{dig_max}{dig_min} {dig_max}{dig_mid}")

