T = int(input())
for x in range(T):
    N = int(input())
    num = [int(i) for i in input().split()][:N]
    for i, e in reversed(list(enumerate(num))):
        if e != 0:
            print(i)
            break
