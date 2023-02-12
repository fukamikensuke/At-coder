N = int(input())
S = list(str(input()))

cnt = 0
for i in range(N):
    if S[i] == '"':
        cnt += 1
    if cnt % 2 == 0:
        if S[i] == ",":
            S[i] = "."
            cnt = 0
    print(S[i], end="")
