import sys

sys.setrecursionlimit(10**6)

N, M = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(M)]
cnt = 0
p = [-1] * N


def root(x):
    # print("x:", x, "p", p[x])
    if p[x] < 0:  ##0以下のものが親ノードとなる
        return x
    # print("P[x]:", p[x], "root[p]", root(p[x]))
    p[x] = root(p[x])
    # print("2P[x]:", p[x], "root[p]", root(p[x]))
    return p[x]


def unite(x, y):
    x = root(x)
    y = root(y)
    # print("x:y", x, y)
    if x == y:
        return
    p[x] -= 1  ##子ノードを配下に置く
    p[y] = x  ##親ノードを入れる


degree = [0] * N  ## エッジの数を保存する
# print("P", p)
# print("degree:", degree)

for i in range(M):
    a, b = AB[i]
    a -= 1
    b -= 1
    # print(a, b)
    degree[a] += 1
    degree[b] += 1
    if root(a) == root(b):  ##親ノードが何かを探索 =>閉路か否かの探索
        cnt += 1
    # print("UNITE")
    unite(a, b)  ##a,bをつなぐ
    # print("P", p)
    # print("degree:", degree)

print(cnt)
