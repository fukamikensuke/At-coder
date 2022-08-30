a,b = map(int,input().split())

x = (a*b)%2

if x==1:
    print("Odd")
else:
    print("Even")