a = int(input())
b = int(input())
c = int(input())
max_s = max(a, b, c)
min_s = min(a, b, c)
if min_s < a < max_s:
    mid_s = a
elif min_s < b < max_s:
    mid_s = b
else:
    mid_s = c
if max_s ** 2 == mid_s ** 2 + min_s ** 2:
    print("100%")
elif max_s ** 2 > mid_s ** 2 + min_s ** 2:
    print("велика")
elif max_s ** 2 < mid_s ** 2 + min_s ** 2:
    print("крайне мала")
