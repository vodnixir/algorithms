def go(start, cur):
    if len(cur) == k:
        res.append(' '.join(map(str, cur)))
        return
    for x in range(start, n + 1):
        cur.append(x)
        go(x + 1, cur)
        cur.pop()


n, k = map(int, input().split())
res = []
go(1, [])
print(len(res))
print('\n'.join(res))
