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


class IterExhausted(BaseException):
    pass


class TwoListIter:
    def __init__(self, l_1, l_2):
        self.l_1 = l_1
        self.l_2 = l_2

        self.ptr_1 = 0
        self.ptr_2 = 0
        self.counter = 0
        self.length = len(l_1) + len(l_2)

    def next(self):
        if not self._has_next():
            raise IterExhausted("no more elems")

        # if bother list has not ehaust
        if self.ptr_1 < len(self.l_1) and self.ptr_2 < len(self.l_2):
            if self.l_1[self.ptr_1] < self.l_2[self.ptr_2]:
                rslt = self.l_1[self.ptr_1]
                self.ptr_1 += 1
                self.counter += 1

            else:
                rslt = self.l_2[self.ptr_2]
                self.ptr_2 += 1
                self.counter += 1

            return rslt
        # one of the list ehaust
        else:
            # find which list not ehaust
            # l_1 is valid
            if self.ptr_1 < len(self.l_1):
                rslt = self.l_1[self.ptr_1]
                self.ptr_1 += 1
                self.counter += 1
                return rslt
            # l_2 is valid
            else:
                rslt = self.l_2[self.ptr_2]
                self.ptr_2 += 1
                self.counter += 1

                return rslt

    def _has_next(self):
        if self.counter < self.length:
            return True
        else:
            return False


a = [1, 5, 6, 8]

b = [2, 3, 9, 10]

it = TwoListIter(a, b)

for i in range(20):
    if it._has_next():
        print(f"main call:{it.next()}")

# print(it.next())
# while(it.has_next()):
#     print(f"main call:{it.next()}")



