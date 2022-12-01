password = input()
dig_1 = int(password[0:1])
dig_2 = int(password[1:2])
dig_3 = int(password[2:3])
sum_1 = dig_2 + dig_3
sum_2 = dig_1 + dig_2
print(max(sum_1, sum_2), min(sum_1, sum_2), sep="")
