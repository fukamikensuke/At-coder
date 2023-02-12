n = int(input())

output = f"{n:X}"
if len(output) == 1:
    output = f"0{n:X}"

print(output)
