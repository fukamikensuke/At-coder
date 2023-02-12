H,W= map(int, input().split())
cnt = 0
for i in range(H):
    a = list(str(input()))
    cnt +=a.count('#')
print(cnt)