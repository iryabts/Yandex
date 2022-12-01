num = input()
dig_1 = int(num[0:1])
dig_2 = int(num[1:2])
dig_3 = int(num[2:3])
max_dig = max(dig_1, dig_2, dig_3)
min_dig = min(dig_1, dig_2, dig_3)
if dig_1 < dig_2 < dig_3 or dig_3 < dig_2 < dig_1:
    mid_dig = dig_2
elif dig_2 < dig_1 < dig_3 or dig_3 < dig_1 < dig_2:
    mid_dig = dig_1
else:
    mid_dig = dig_3
if min_dig + max_dig == mid_dig * 2:
    print("YES")
else:
    print("NO")
