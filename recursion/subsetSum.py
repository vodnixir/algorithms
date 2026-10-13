def go(i, cur, cnt):
    if i == n:
        return cur == s and cnt > 0
    return go(i + 1, cur + a[i], cnt + 1) or go(i + 1, cur, cnt)


n = int(input())
a = list(map(int, input().split()))
s = int(input())
print('Yes' if go(0, 0, 0) else 'No')
