A, B, C, D, E, F = map(int, input().split())

s = (A * B * C) - (D * E * F)

print(s % 998244353)
