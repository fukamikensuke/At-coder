N, K = map(int, input().split())
ranking = []
for i in range(K):
    ranking.append(input())

ranking.sort()
for i in ranking:
    print(i)
