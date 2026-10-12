from bisect import bisect_right, insort


def sort(a):
    if len(a) <= 64:
        b = []
        cnt = 0
        for i, x in enumerate(a):
            cnt += i - bisect_right(b, x)
            insort(b, x)
        return b, cnt
    mid = len(a) // 2
    left, x = sort(a[:mid])
    right, y = sort(a[mid:])
    cnt = x + y + len(left) * len(right)
    for v in right:
        cnt -= bisect_right(left, v)
    return sorted(left + right), cnt


n = int(input())
a = list(map(int, input().split()))
print(sort(a)[1])
