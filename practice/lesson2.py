#四則計算する関数'add'の作成
def _cal(x:int,y:int):
    return x+y,x-y,x*y,x/y

#list に対するを計算する関数
def l_cal(a,b):
    s = []
    for i,j in zip(a,b):
        s.append(i+ j)
    return s

#listに対する計算--v2(error)
def l_cal_v2(a,b):
    s = []
    if len(a) != len(b):
        return "error"
    else: 
        for i,j in zip(a,b):
            s.append(i+ j)
    return s


a = int(input())
b = int(input())

print(_cal(a,b))
