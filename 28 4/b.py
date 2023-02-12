T = int(input())
for i in range(T):
    cnt = 0
    N = int(input())
    test = list(map(int, input().split()))
    for j in test:
        if j % 2 != 0:
            cnt += 1
    print(cnt)