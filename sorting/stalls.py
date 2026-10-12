import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(m):
    b, e = map(int, input().split())
    a.append((b, e))
a.sort()
cnt = 0
l, r = a[0]
for b, e in a[1:]:
    if b <= r + 1:
        r = max(r, e)
    else:
        cnt += r - l + 1
        l, r = b, e
cnt += r - l + 1
print(n - cnt)
