import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))
heapq.heapify(a)
for _ in range(k - 1):
    heapq.heappop(a)
print(a[0])
