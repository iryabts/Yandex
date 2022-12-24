V_Pete = int(input())
V_Vasya = int(input())
V_Tolya = int(input())
if V_Pete >= V_Vasya and V_Pete >= V_Tolya:
    print("Петя")
elif V_Vasya >= V_Pete and V_Vasya >= V_Tolya:
    print("Вася")
else:
    print("Толя")
