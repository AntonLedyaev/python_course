objects = [1, 2, 1, 2, 3]
tmp = []
for obj in objects:
    if not obj in tmp:
        tmp.append(obj)
ans = len(tmp)
