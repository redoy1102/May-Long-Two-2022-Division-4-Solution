T = int(input())
for x in range(T):
    N = int(input())
    n = 4
    num = [int(i) for i in input().split()][:n]
    print(max(num))