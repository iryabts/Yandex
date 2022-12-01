first = int(input())
last = int(input())
if 0 <= first <= last:
    for i in range(first, last + 1, 1):
        print(i, end=" ")
elif last <= 0 <= first:
    for i in range(first, last - 1, -1):
        print(i, end=" ")
elif first <= 0 <= last:
    for i in range(first, last + 1):
        print(i, end=" ")
elif last <= first <= 0:
    for i in range(first, last - 1, -1):
        print(i, end=" ")
elif first <= last <= 0:
    for i in range(first, last + 1):
        print(i, end=" ")
elif first >= last:
    for i in range(first, last - 1, -1):
        print(i, end=" ")
