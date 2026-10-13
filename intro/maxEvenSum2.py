a = list(map(int, input().split()))
s = sum(a)
if s % 2 == 1:
    s -= min(x for x in a if x % 2 == 1)
print(s)
