n = input()
m = input()
n_d_1 = int(n[0:1])
n_d_2 = int(n[1:2])
m_d_1 = int(m[0:1])
m_d_2 = int(m[1:2])
max_d = max(n_d_1, n_d_2, m_d_1, m_d_2)
min_d = min(n_d_1, n_d_2, m_d_1, m_d_2)
if max_d == n_d_1 and min_d == n_d_2 or max_d == n_d_2 and min_d == n_d_1:
    rest = m_d_1 + m_d_2
elif max_d == m_d_1 and min_d == m_d_2 or max_d == m_d_2 and min_d == m_d_1:
    rest = n_d_1 + n_d_2
elif max_d == n_d_1 and min_d == m_d_1 or max_d == m_d_1 and min_d == n_d_1:
    rest = n_d_2 + m_d_2
elif max_d == n_d_1 and min_d == m_d_2 or max_d == m_d_2 and min_d == n_d_1:
    rest = n_d_2 + m_d_1
elif max_d == n_d_2 and min_d == m_d_1 or max_d == m_d_1 and min_d == n_d_2:
    rest = n_d_1 + m_d_2
else:
    rest = n_d_1 + m_d_1
rest = str(rest)
if rest[1:2] != "":
    print(max_d, rest[1:2], min_d, sep="")
else:
    print(max_d, rest[0:1], min_d, sep="")
