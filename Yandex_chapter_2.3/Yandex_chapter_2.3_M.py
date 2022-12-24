n = int(input())
name = input()
for i in range(n - 1):
    name_2 = input()
    if name == min(name, name_2):
        name = name
    elif name_2 == min(name, name_2):
        name = name_2
print(name)
