# 273. Integer to English Words
# Hard
#
# Convert a non-negative integer num to its English words representation.
#
# Example 1:
#
# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:
#
# Input: num = 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
# 0 <= num <= 231 - 1

class Solution:
    under20 = ["One", "Two", "Three", "Four", "Five",
               "Six", "Seven", "Eight", "Nine", "Ten",
               "Eleven", "Twelve", "Thirteen", "Fourteen",
               "Fifteen", "Sixteen", "Seventeen", "Eighteen",
               "Nineteen"]
    under100 = ["Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]

    HTMB = ["Hundred", "Thousand", "Million", "Billion"]
    P = [100, 1000, 1000 * 1000, 1000 * 1000 * 1000]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self.convert(num)[1:]

    def convert(self, num):
        if num == 0:
            return ""
        if num < 20:
            return " " + Solution.under20[num - 1]
        if num < 100:
            return " " + Solution.under100[num // 10 - 2] + self.convert(num % 10)
        for i in [3, 2, 1, 0]:
            if num >= Solution.P[i]:
                return self.convert(num // Solution.P[i]) + " " + Solution.HTMB[i] + self.convert(
                    num % Solution.P[i])
        return ""


sol = Solution()
sol.numberToWords(81)
sol.numberToWords(num=1234567891)
