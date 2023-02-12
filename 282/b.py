N, M = map(int, input().split())
cnt = N * (N - 1) / 2
S = []
for i in range(N):
    S.append(list(str(input())))
    for j in range(0, i):
        for k in range(M):
            if S[i][k] == "x":
                if S[j][k] == "x":
                    cnt -= 1
                    break

print(int(cnt))
