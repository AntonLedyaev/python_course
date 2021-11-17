parents = 'parent_namespaces'
vars = 'vars'
scopes = {'global': {parents: '', vars: []}}

def create(namespace, parent):
    if namespace not in scopes:
        scopes[namespace] = {parents: parent, vars: []}

def add(namespace, var):
    if namespace in scopes:
        scopes[namespace][vars].append(var)

def get(namespace, var):
    if namespace == 'global':
        print('None' if var not in scopes[namespace][vars] else namespace)
    elif var in scopes[namespace][vars]:
        print(namespace)
    else:
        get(scopes[namespace][parents], var)

funcs = {'create': create, 'add': add, 'get': get}
n = int(input())
for _ in range(n):
    cmd, p1, p2 = input().split()
    funcs[cmd](p1, p2)


