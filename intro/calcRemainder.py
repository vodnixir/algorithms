n, m = map(int, input().split())
s = input().strip()
cur = 0
res = []
for c in s:
    cur = (cur * 10 + int(c)) % m
    res.append(cur)
print(*res)
