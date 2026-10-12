import sys

input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    s, c, p = input().split()
    a.append((-int(c), int(p), s))
a.sort()
print('\n'.join(x[2] for x in a))
