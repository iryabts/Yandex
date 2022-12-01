V_Pete = int(input())
V_Vasya = int(input())
V_Tolya = int(input())
s = 43872
if s / V_Pete <= s / V_Vasya and s / V_Pete <= s / V_Tolya:
    print("Петя")
elif s / V_Vasya <= s / V_Pete and s / V_Vasya <= s / V_Tolya:
    print("Вася")
elif s / V_Tolya <= s / V_Pete and s / V_Tolya <= s / V_Vasya:
    print("Толя")
