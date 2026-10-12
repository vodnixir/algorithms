import sys

input = sys.stdin.readline


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.h = 1


def h(t):
    return t.h if t else 0


def upd(t):
    t.h = max(h(t.left), h(t.right)) + 1


def bal(t):
    return h(t.right) - h(t.left)


def rot_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    upd(a)
    upd(b)
    return b


def rot_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    upd(a)
    upd(b)
    return b


def balance(v):
    upd(v)
    if bal(v) == 2:
        if bal(v.right) < 0:
            v.right = rot_right(v.right)
        return rot_left(v)
    if bal(v) == -2:
        if bal(v.left) > 0:
            v.left = rot_left(v.left)
        return rot_right(v)
    return v


def add(t, x):
    if t is None:
        return Node(x)
    if x < t.key:
        t.left = add(t.left, x)
    elif x > t.key:
        t.right = add(t.right, x)
    else:
        return t
    return balance(t)


def exists(t, x):
    while t is not None:
        if x == t.key:
            return True
        if x < t.key:
            t = t.left
        else:
            t = t.right
    return False


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
    elif cmd[0] == 'exists':
        out.append('YES' if exists(root, int(cmd[1])) else 'NO')
    elif cmd[0] == 'root':
        out.append(str(root.key) if root else 'Empty')
    elif cmd[0] == 'height':
        out.append(str(h(root)))
    else:
        res = []
        preorder(root, res)
        out.append(' '.join(res) if res else 'Empty')

print('\n'.join(out))
