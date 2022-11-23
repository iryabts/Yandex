n = input()
n_dig_1 = int(n[0:1])
n_dig_2 = int(n[1:2])
n_dig_3 = int(n[2:3])
dig_min = min(n_dig_1, n_dig_2, n_dig_3)
dig_max = max(n_dig_1, n_dig_2, n_dig_3)
if n_dig_2 < n_dig_1 < n_dig_3 or n_dig_3 < n_dig_1 < n_dig_2:
    n_dig_mid = n_dig_1
elif n_dig_1 < n_dig_2 < n_dig_3 or n_dig_3 < n_dig_2 < n_dig_1:
    n_dig_mid = n_dig_2
else:
    n_dig_mid = n_dig_3
if dig_min == 0:
    print(n_dig_mid, dig_min, " ", dig_max, n_dig_mid, sep="")
else:
    print(dig_min, n_dig_mid, " ", dig_max, n_dig_mid, sep="")
