import math
S = list(str(input()))
T = list(str(input()))

i = round(len(T)/2)-1
print(i)
cnt = 0
start = 0
end = len(T)-1
while   start!=end:
    if S[i] == T[i]:
        start = i
        print(S[i],"=",T[i],)
        i = start + round((end-start)//2)
    elif S[i] != T[i]:
        end = i
        print(S[i],"!=",T[i],i)
        i = start + round((end-start)/2)
    
print(i)