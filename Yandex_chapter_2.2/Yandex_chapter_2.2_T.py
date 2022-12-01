str_1 = input()
str_2 = input()
str_3 = input()
if "зайка" in str_1:
    repl_1 = True
else:
    repl_1 = False
if "зайка" in str_2:
    repl_2 = True
else:
    repl_2 = False
if "зайка" in str_3:
    repl_3 = True
else:
    repl_3 = False
len_1 = len(str_1)
len_2 = len(str_2)
len_3 = len(str_3)
if repl_1 and repl_2 and repl_3 and str_1 == min(str_1, str_2, str_3):
    print(str_1, len_1)
elif repl_1 and repl_2 and repl_3 and str_2 == min(str_1, str_2, str_3):
    print(str_2, len_2)
elif repl_1 and repl_2 and repl_3 and str_3 == min(str_1, str_2, str_3):
    print(str_3, len_3)
elif not repl_1 and repl_2 and repl_3 and str_2 == min(str_2, str_3):
    print(str_2, len_2)
elif not repl_1 and repl_2 and repl_3 and str_3 == min(str_2, str_3):
    print(str_3, len_3)
elif repl_1 and not repl_2 and repl_3 and str_1 == min(str_1, str_3):
    print(str_1, len_1)
elif repl_1 and not repl_2 and repl_3 and str_3 == min(str_1, str_3):
    print(str_3, len_3)
elif repl_1 and repl_2 and not repl_3 and str_2 == min(str_1, str_2):
    print(str_2, len_2)
elif repl_1 and repl_2 and not repl_3 and str_1 == min(str_1, str_2):
    print(str_1, len_1)
elif repl_1 and not repl_2 and not repl_3:
    print(str_1, len_1)
elif repl_2 and not repl_1 and not repl_3:
    print(str_2, len_2)
elif repl_3 and not repl_1 and not repl_2:
    print(str_3, len_3)
