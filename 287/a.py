N = int(input())
cnt = 0
for i in range(N):
    if input() == "For":
        cnt += 1
    if cnt >N/2:
        print("Yes")
        exit()
print("No")