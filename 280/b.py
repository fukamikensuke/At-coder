N = int(input())

S = list(map(int, input().split()))
A = []
s = 0
A.append(S[0])
for i in range(1,N):
    s += A[i-1]
    A.append(S[i]-s)

print(*A)