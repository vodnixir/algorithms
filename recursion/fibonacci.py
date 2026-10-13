import sys

sys.setrecursionlimit(300000)


def fib(n):
    if n <= 1:
        return 1 % m
    if memo[n] == -1:
        memo[n] = (fib(n - 1) + fib(n - 2)) % m
    return memo[n]


n, m = map(int, input().split())
memo = [-1] * (n + 1)
print(fib(n))
