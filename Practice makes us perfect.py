P1, P2, P3, P4 = map(int, input().split())
c = 0

if P1 >= 10:
    c = c + 1
if P2 >= 10:
    c = c + 1
if P3 >= 10:
    c = c + 1
if P4 >= 10:
    c = c + 1

print(c)
