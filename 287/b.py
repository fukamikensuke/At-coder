N,M = map(int, input().split())
S = []
T = []
cnt = 0
for i in range(N):
    _S = input()
    s = list(_S)
    S.append(s[3]+s[4]+s[5])
for i in range(M):
    T .append(input())

T = list(set(T))
for i in T :
    for j in S:
        if i == j:
            cnt +=1

print(cnt)