# N = int(input())


# def cal(k: int):
#     sum = 0
#     if k == 0:
#         return 1
#     else:
#         print(k // 2, k // 3)
#         sum = cal(round(k // 2)) + cal(round(k // 3))

#     return sum


# print(cal(N))

from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 1
    print(n // 2, n // 3)
    return f(n // 2) + f(n // 3)


print(f(int(input())))
