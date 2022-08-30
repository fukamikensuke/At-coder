n = int (input())
a = [n]   
a =  list(map(int, input().split()))

alce = 0
bob = 0
max = 0
newlist = sorted(a, reverse=True)
   


for i in range (0,n):

    if (i+1)%2 ==  1:
        alce += newlist[i]
    else :
        bob += newlist[i]

sum = alce - bob
print (sum)