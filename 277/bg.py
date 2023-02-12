N = int(input())
S = []
for i in range(N):
    _s = str(input())
    if _s[0] == "H" or _s[0] == "D" or _s[0] == "C" or _s[0] == "S":
        if (
            _s[1] == "A"
            or _s[1] == "2"
            or _s[1] == "3"
            or _s[1] == "4"
            or _s[1] == "5"
            or _s[1] == "6"
            or _s[1] == "7"
            or _s[1] == "8"
            or _s[1] == "9"
            or _s[1] == "T"
            or _s[1] == "J"
            or _s[1] == "Q"
            or _s[1] == "K"
        ):
            if _s in S:
                print("No")
                break
            else:
                S.append(_s)
        else:
            print("No")
            break
    else:
        print("No")
        break
    if i == N - 1:
        print("Yes")
