## 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。
a = [3]   
a =  list(map(int, input().split()))

sum = 0

for i in range (1,a[0]+1):
    lst = []
    num = 0
    tmp = i
    while i > 0:
        lst.append(i%10)
        i //= 10
    for  j in range(len(lst)):
        num += int(lst[j])
    if num >= a[1]:
        if num <= a[2]:
            sum += tmp
print (sum)
