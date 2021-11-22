exceptions = {}
throwed_exceptions = []


def found_path(exceptions, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in exceptions:
        return []
    for node in exceptions[start]:
        if node not in path:
            new_path = found_path(exceptions, node, end, path)
            if new_path:
                return new_path
    return []


n = int(input())
for _ in range(n):
    input_value = input().split()
    child = input_value[0]
    parents = input_value[2:]
    exceptions[child] = parents

m = int(input())
for _ in range(m):
    throwing_exception = input()
    for throwed_exception in throwed_exceptions:
        if len(found_path(exceptions, throwing_exception, throwed_exception)) > 1:
            print(throwing_exception)
            break
        throwed_exceptions.append(throwing_exception)
