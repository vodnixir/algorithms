def go(i, cur):
    if i == n:
        return cur == s and len(path) > 0
    path.append(a[i])
    if go(i + 1, cur + a[i]):
        return True
    path.pop()
    return go(i + 1, cur)


n = int(input())
a = list(map(int, input().split()))
s = int(input())
path = []
if go(0, 0):
    print('Yes')
    print(len(path))
    print(*path)
else:
    print('No')
