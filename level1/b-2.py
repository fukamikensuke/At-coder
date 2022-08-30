

a = int(input())
b = int(input())
c = int(input())
x = int(input())



sum = 0
for a_cnt in range(0,a+1):
    for b_cnt in range(0,b+1):
        for c_cnt in range(0,c+1):
            if x == 500*a_cnt+100*b_cnt+50*c_cnt:
                sum += 1

print(sum)