# def func(n, k):
#     end = n // k
#     start = 1
#
#     rslt = (start + end) * end / 2 * k
#
#     return rslt
#
#
# # print(func(1000,3))
#
#
# print(func(1000, 3) + func(1000, 5) - func(1000, 15))
#
"""
a = [1, 5, 6, 8, ]

b = [2, 3, 9, 10]

m = MergeIter(...)

m.next() # 1
m.next() # 2
m.next() # 3
m.next() # 5

for i in range(5):
    print(m.next())
"""


class TwoListIter:
    def __init__(self, l_1, l_2):
        self.l_1 = l_1
        self.l_2 = l_2

        self.ptr_1 = 0
        self.ptr_2 = 0
        self.counter = 0
        self.length = len(l_1) + len(l_2)

    def next(self):

        if self.l_1[self.ptr_1] > self.l_2[self.ptr_2]:
            rslt = self.l_1[self.ptr_1]
            self.ptr_1 += 1
            self.counter += 1

        else:
            rslt = self.l_2[self.ptr_2]
            self.ptr_2 += 1
            self.counter += 1

        return rslt

    def has_next(self):
        if self.counter < self.length:
            return True
        else:
            return False


a = [1, 5, 6, 8]

b = [2, 3, 9, 10]

it = TwoListIter(a, b)

print(it.next())
# while(it.has_next()):
#     print(f"main call:{it.next()}")
