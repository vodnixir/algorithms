import sys


def main():
    a = list(map(int, sys.stdin.buffer.read().split()))
    ps = [10 ** 9]
    cs = [0]
    res = []
    for p in a:
        c = 1
        while ps[-1] <= p:
            ps.pop()
            c += cs.pop()
        ps.append(p)
        cs.append(c)
        res.append(c)
    print(' '.join(map(str, res)))


main()
