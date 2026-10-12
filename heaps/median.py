import sys
import heapq

input = sys.stdin.readline

q = int(input())
lo = []
hi = []
out = []
for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'ADD':
        x = int(cmd[1])
        if lo and x > -lo[0]:
            heapq.heappush(hi, x)
        else:
            heapq.heappush(lo, -x)
        if len(lo) > len(hi) + 1:
            heapq.heappush(hi, -heapq.heappop(lo))
        elif len(hi) > len(lo):
            heapq.heappush(lo, -heapq.heappop(hi))
    else:
        out.append(str(-lo[0]))
print('\n'.join(out))
