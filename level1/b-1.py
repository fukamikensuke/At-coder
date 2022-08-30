n = int(input())
a = [n]   
a =  list(map(int, input().split()))

out_cnt = 0
Odd_cnt = 0
while Odd_cnt == 0:
    for i in range(0,n):
        if a[i] % 2 == 0 :
            a[i] = a[i]/2
        else :
            Odd_cnt = 1
    if Odd_cnt == 0:
        out_cnt += 1

print(out_cnt)