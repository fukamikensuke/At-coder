N, X = map(int, input().split())
P = list(map(int, input().split()))


for i in range(0, N):
    if X == P[i]:
        print(i + 1)
