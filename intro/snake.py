n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
top, bottom, left, right = 0, n - 1, 0, m - 1
res = []
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        res.append(a[top][j])
    for i in range(top + 1, bottom + 1):
        res.append(a[i][right])
    if top < bottom:
        for j in range(right - 1, left - 1, -1):
            res.append(a[bottom][j])
    if left < right:
        for i in range(bottom - 1, top, -1):
            res.append(a[i][left])
    top += 1
    bottom -= 1
    left += 1
    right -= 1
print(*res)
