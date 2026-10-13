def move(n, a, b, c):
    if n == 0:
        return
    move(n - 1, a, c, b)
    res.append(f'{n} {a} {c}')
    move(n - 1, b, a, c)


n = int(input())
res = []
move(n, 1, 2, 3)
print(len(res))
print('\n'.join(res))
