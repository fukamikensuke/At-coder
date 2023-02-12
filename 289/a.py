s = input()

s = list(s)

if s[0] == "0":
    s[0] = 1
else:
    s[0] = 0

output = str(s[0])
for i in range(1, len(s)):
    if s[i] == "0":
        s[i] = 1
    else:
        s[i] = 0
    output = output + str(s[i])
print(output)
