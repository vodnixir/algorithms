import sys

input = sys.stdin.readline


class Deque:
    def __init__(self, n):
        self.a = [0] * n
        self.head = n // 2
        self.tail = n // 2

    def push_back(self, x):
        self.a[self.tail] = x
        self.tail += 1

    def push_front(self, x):
        self.head -= 1
        self.a[self.head] = x

    def pop_back(self):
        self.tail -= 1
        return self.a[self.tail]

    def pop_front(self):
        x = self.a[self.head]
        self.head += 1
        return x

    def back(self):
        return self.a[self.tail - 1]

    def front(self):
        return self.a[self.head]

    def size(self):
        return self.tail - self.head


q = int(input())
d = Deque(2 * q + 1)
out = []
for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'push':
        if cmd[1] == 'back':
            d.push_back(int(cmd[2]))
        else:
            d.push_front(int(cmd[2]))
    elif cmd[0] == 'size':
        out.append(str(d.size()))
    elif d.size() == 0:
        out.append('Error')
    elif cmd[0] == 'pop':
        out.append(str(d.pop_back() if cmd[1] == 'back' else d.pop_front()))
    else:
        out.append(str(d.back() if cmd[1] == 'back' else d.front()))
print('\n'.join(out))
