a = list(map(int, input().split()))
r = [[], [], []]
for x in a:
    r[x % 3].append(x)
ans = -1
if r[1] and r[2]:
    ans = max(r[1]) + max(r[2])
if len(r[0]) >= 2:
    r[0].sort()
    ans = max(ans, r[0][-1] + r[0][-2])
print(ans)
