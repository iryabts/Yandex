num_1 = input()
num_2 = input()
num_3 = input()
num_1_d_1 = num_1[0:1]
num_1_d_2 = num_1[1:2]
num_2_d_1 = num_2[0:1]
num_2_d_2 = num_2[1:2]
num_3_d_1 = num_3[0:1]
num_3_d_2 = num_3[1:2]
if num_1_d_1 == num_2_d_1 == num_3_d_1:
    print(num_1_d_1)
elif num_1_d_2 == num_2_d_2 == num_3_d_2:
    print(num_1_d_2)
