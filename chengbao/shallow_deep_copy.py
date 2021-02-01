from copy import deepcopy, copy
l_1 = [1, 2]
l_2 = [3, 4]
a = [l_1, l_2]

a
b = copy(a)
id(b)
id(a)

b[0][0]=-100
b
a