N, Q = map(int, input().split())

L = [list(map(int, input().split())) for i in range(N)]
S = [list(map(int, input().split())) for i in range(Q)]

for i in S:
    print(L[i[0] - 1][i[1]])
