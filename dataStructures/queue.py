import sys

input = sys.stdin.readline


class Queue:
    def __init__(self):
        self.a = []
        self.head = 0

    def push(self, x):
        self.a.append(x)

    def pop(self):
        x = self.a[self.head]
        self.head += 1
        return x

    def get(self):
        return self.a[self.head]

    def size(self):
        return len(self.a) - self.head


q = int(input())
que = Queue()
out = []
for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'push':
        que.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        out.append(str(que.pop()) if que.size() > 0 else 'Error')
    elif cmd[0] == 'get':
        out.append(str(que.get()) if que.size() > 0 else 'Error')
    else:
        out.append(str(que.size()))
print('\n'.join(out))
