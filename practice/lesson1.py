#10000までの素数を表示するプログラミング
s = []
s.append(2)
for i in range(2,100):
    if i % 2 != 0:
        cnt = 0
        for j in s:
            if i % j == 0:
                cnt +=1
            if cnt > 0:
                break
        if cnt == 0:
            s.append(i)

print(s)