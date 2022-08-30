n = int (input())
d = [n] 
for i in range(0,n):
    print(len(d))
    d[i] = int (input())

for i in range (0,n):
    for j in range (i,n):
        if d[i]  == d[j]:
            d.pop(j)

print(len(d))