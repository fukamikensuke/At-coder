import numpy as np

N = int(input())
H = list(map(int, input().split()))

a = np.array(H)

print((np.argmax(a)) + 1)
