n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
i = j = 0
while i < n and j < m:
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
res += a[i:]
res += b[j:]
print(*res)
