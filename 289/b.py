N, M = map(int, input().split())
a = list(map(int, input().split()))

num_connect = []
num_list = list(range(1, N + 1))
for i in range(M):
    if i[i] + 1 == i[i + 1]:
        num_connect.append(i)
        num_connect.append(i + 1)
    else:
        num_connect[len(num_connect) - 1]
