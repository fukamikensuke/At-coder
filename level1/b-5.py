n = int(input())
l = []
for i in range(0, n):
    d = int(input())
    l.append(d)

print(len(list(set(l))))
