def go(r):
    if r == n:
        res.append(' '.join(map(str, cur)))
        return
    for c in range(1, n + 1):
        if c in cols or r - c in d1 or r + c in d2:
            continue
        cols.add(c)
        d1.add(r - c)
        d2.add(r + c)
        cur.append(c)
        go(r + 1)
        cur.pop()
        cols.remove(c)
        d1.remove(r - c)
        d2.remove(r + c)


n = int(input())
cols = set()
d1 = set()
d2 = set()
cur = []
res = []
go(0)
print(len(res))
if res:
    print('\n'.join(res))
