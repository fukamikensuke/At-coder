# N = int(input())

# for i in range(N):
#     start,end = map(int, input().split())
#     if start > end :
#         max
m = 1
s = sorted
_, *L = open(0)
for a, b in s(s(map(int, t.split())) for t in L):
    m = (m, b)[a <= m < b]
print(m)
