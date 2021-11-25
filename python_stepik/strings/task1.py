s, a, b = (input() for _ in range(3))
count = 0
flag = True
while a in s:
    s = s.replace(a, b)
    count += 1
    if count == 1000:
        count = "Impossible"
        break

print(count)
