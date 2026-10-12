import sys
import heapq

input = sys.stdin.readline

k = int(input())
a = []
for _ in range(k):
    a.append(list(map(int, input().split()))[1:])
h = []
for i in range(k):
    heapq.heappush(h, (a[i][0], i, 0))
res = []
while h:
    x, i, j = heapq.heappop(h)
    res.append(x)
    if j + 1 < len(a[i]):
        heapq.heappush(h, (a[i][j + 1], i, j + 1))
print(*res)
