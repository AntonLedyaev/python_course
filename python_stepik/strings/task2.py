
s, t = input(), input()

count = 0

for i in range(len(s)):
    if s.startswith(t, i):
        count += 1





print(count)
