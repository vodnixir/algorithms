n = int(input())
a = list(map(int, input().split()))
s = int(input())
b = sorted(range(n), key=lambda i: a[i])
l, r = 0, n - 1
while l < r:
    cur = a[b[l]] + a[b[r]]
    if cur == s:
        i, j = b[l] + 1, b[r] + 1
        print(min(i, j), max(i, j))
        break
    if cur < s:
        l += 1
    else:
        r -= 1
else:
    print(-1)
