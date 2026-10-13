a = list(map(int, input().split()))
s = sum(a)
r1 = sorted(x for x in a if x % 3 == 1)
r2 = sorted(x for x in a if x % 3 == 2)
if s % 3 == 0:
    print(s)
else:
    if s % 3 == 1:
        one, two = r1, r2
    else:
        one, two = r2, r1
    best = 0
    if one:
        best = max(best, s - one[0])
    if len(two) >= 2:
        best = max(best, s - two[0] - two[1])
    print(best)
