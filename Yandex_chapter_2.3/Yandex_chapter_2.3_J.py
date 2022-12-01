x = 0
y = 0
while (a := input()) != "СТОП":
    b = int(input())
    if a == "СЕВЕР":
        y = y + b
    elif a == "ЮГ":
        y = y - b
    elif a == "ВОСТОК":
        x = x + b
    elif a == "ЗАПАД":
        x = x - b
print(y)
print(x)
