# 390. Elimination Game
# Medium
#
# There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other
# number afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left, remove the right most number and every other number
# from the remaining numbers.
# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
# Find the last number that remains starting with a list of length n.
#
# Example:
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
#
# Output:
# 6

class Solution:
    def lastRemaining(self, n: int) -> int:
        numbers = list(range(1, n + 1))
        print(numbers)
        remove_from_right = False
        while len(numbers) > 1:
            index = list(range(0, len(numbers)))
            if not remove_from_right:
                index = [i for i in index if i % 2 != 0]
                numbers = [numbers[i] for i in index]
                print(numbers)
            else:
                if len(numbers) % 2 == 1:
                    index = [i for i in index if i % 2 != 0]
                    numbers = [numbers[i] for i in index]
                    print(numbers)
                else:
                    index = [i for i in index if i % 2 != 1]
                    numbers = [numbers[i] for i in index]
                    print(numbers)

            remove_from_right = not remove_from_right
        return numbers[0]
