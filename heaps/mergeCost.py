import heapq

n = int(input())
a = list(map(int, input().split()))
heapq.heapify(a)
ans = 0
while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    ans += x + y
    heapq.heappush(a, x + y)
print(ans)
