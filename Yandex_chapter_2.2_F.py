year = int(input())
vis_1 = year % 4
vis_2 = year % 100
vis_3 = year % 400
if vis_1 == 0 and vis_2 != 0 or vis_2 == 0 and vis_3 == 0:
    print("YES")
else:
    print("NO")
