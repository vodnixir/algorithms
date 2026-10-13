a = list(map(int, input().split()))
ev = sorted([x for x in a if x % 2 == 0], reverse=True)
od = sorted([x for x in a if x % 2 == 1], reverse=True)
ans = -1
if len(ev) >= 2:
    ans = ev[0] + ev[1]
if len(od) >= 2:
    ans = max(ans, od[0] + od[1])
print(ans)
