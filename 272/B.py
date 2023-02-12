import numpy as np

N,M= map(int, input().split())
k = [list(map(int, input().split())) for i in range(N)]
a = np.array(k)
cnt = []

for i in range(0,N):
    for j in range(0,M):
    
