T = int(input())
for x in range(T):
    X, Y = map(int, input().split())

    total_prize_money = ((10*X) + (90*Y))
    print(total_prize_money)
