name_1 = input()
name_2 = input()
name_3 = input()
if len(name_1) < len(name_2) and len(name_1) < len(name_3):
    print(name_1)
elif len(name_2) < len(name_1) and len(name_2) < len(name_3):
    print(name_2)
else:
    print(name_3)
# elif len(name_3) <= len(name_2) and len(name_3) <= len(name_1):
#    print(name_3)
