from functools import cmp_to_key


def cmp(x, y):
    if x + y > y + x:
        return -1
    if x + y < y + x:
        return 1
    return 0


n = int(input())
a = input().split()
a.sort(key=cmp_to_key(cmp))
res = ''.join(a)
if res[0] == '0':
    res = '0'
print(res)
