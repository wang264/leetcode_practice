class Stack:
    def __init__(self):
        self.array = []

    def push(self, x):
        self.array.append(x)

    def pop(self):
        return self.array.pop()


s = Stack()

n = 6
for i in range(n):
    s.push(i)

for i in range(6):
    num = s.pop()
    if i % 2 == 0:
        print(num)
