class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(x):
    global root
    if root is None:
        root = Node(x)
        return
    t = root
    while True:
        if x < t.key:
            if t.left is None:
                t.left = Node(x)
                return
            t = t.left
        else:
            if t.right is None:
                t.right = Node(x)
                return
            t = t.right


def find(x):
    p = None
    t = root
    while t.key != x:
        p = t
        if x < t.key:
            t = t.left
        else:
            t = t.right
    return t, p


def left(x):
    global root
    a, p = find(x)
    b = a.right
    a.right = b.left
    b.left = a
    if p is None:
        root = b
    elif p.left is a:
        p.left = b
    else:
        p.right = b


def right(x):
    global root
    a, p = find(x)
    b = a.left
    a.left = b.right
    b.right = a
    if p is None:
        root = b
    elif p.left is a:
        p.left = b
    else:
        p.right = b


def preorder(t, res):
    if t is None:
        return
    res.append(str(t.key))
    preorder(t.left, res)
    preorder(t.right, res)


n = int(input())
root = None
for x in map(int, input().split()):
    add(x)

m = int(input())
out = []
for _ in range(m):
    cmd, x = input().split()
    if cmd == 'left':
        left(int(x))
    else:
        right(int(x))
    res = []
    preorder(root, res)
    out.append(' '.join(res))

print('\n'.join(out))
