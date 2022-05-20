try:
    def MS(M, S):
        return M / S


    T = int(input())
    for x in range(T):
        N = int(input())
        A = [int(i) for i in input().split()][:N]

        if all([i == 0 for i in A]):
            print(0)

        elif A.count(A[0]) == len(A):
            print(1)

        elif all([i % 2 == 0 for i in A]):
            M = max(A)
            S = min(A)
            res_MS = MS(M, S)
            print(int(res_MS))

        elif all([i % 2 != 0 for i in A]):
            M, S = max(A), min(A)
            res_MS = MS(M, S)
            print(int(res_MS))
        else:
            pass


except:
    pass
