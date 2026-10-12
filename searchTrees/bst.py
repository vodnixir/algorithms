import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(t, x):
    if t is None:
        return Node(x)
    if x < t.key:
        t.left = add(t.left, x)
    elif x > t.key:
        t.right = add(t.right, x)
    return t


def delete(t, x):
    if t is None:
        return None
    if x < t.key:
        t.left = delete(t.left, x)
    elif x > t.key:
        t.right = delete(t.right, x)
    else:
        if t.left is None:
            return t.right
        if t.right is None:
            return t.left
        m = t.right
        while m.left is not None:
            m = m.left
        t.key = m.key
        t.right = delete(t.right, m.key)
    return t


def exists(t, x):
    while t is not None:
        if x == t.key:
            return True
        if x < t.key:
            t = t.left
        else:
            t = t.right
    return False


def height(t):
    if t is None:
        return 0
    return max(height(t.left), height(t.right)) + 1


def preorder(t, res):
    if t is None:
        return
    res.append(str(t.key))
    preorder(t.left, res)
    preorder(t.right, res)


q = int(input())
root = None
out = []
for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'add':
        root = add(root, int(cmd[1]))
    elif cmd[0] == 'del':
        root = delete(root, int(cmd[1]))
    elif cmd[0] == 'exists':
        out.append('YES' if exists(root, int(cmd[1])) else 'NO')
    elif cmd[0] == 'height':
        out.append(str(height(root)))
    else:
        res = []
        preorder(root, res)
        out.append(' '.join(res) if res else 'Empty')

print('\n'.join(out))
