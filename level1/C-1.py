n,y = map(int, input().split())

sum = 0
for i in range (0,n+1):
    for j in range (0,n-i+1):
        if 10000*i+5000*j+1000*(n-j-i) == y:
            print(i,j,(n-j-i))
            sum +=1
            break
    if sum >0 :
            break

            

if sum == 0:
    print(-1,-1,-1)    