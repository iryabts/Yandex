n = int(input())
m = int(input())
t = int(input())
total_min = int(n * 60 + m + t)
minutes_to_convert = total_min % (24 * 60)
hours = minutes_to_convert // 60
minutes = minutes_to_convert % 60
print(hours // 10, hours % 10, ":", minutes // 10, minutes % 10, sep="")
