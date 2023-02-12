import numpy as np

N = int(input())
A = list(map(int, input().split()))
a = np.array(A)

for i in range(1, N):
    m = a + a

print(m)
