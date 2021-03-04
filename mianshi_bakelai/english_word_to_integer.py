class Solution:
    small_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                 "ten": 10,
                 "eleventh": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                 "seventeen": 17,
                 "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
                 "seventy": 70, "eighty": 80, "ninety": 90}

    big_num = {"thousand": 1000, "million": 1000000, "billion": 1000000000}

    def word_to_numb(self, s: str):
        arr = s.split(" ")
        arr = [a.lower() for a in arr]
        if s == "zero":
            return 0
        temp_num = 0
        final_num = 0
        for word in arr:
            if word in Solution.small_num:
                temp_num += Solution.small_num[word]
            elif word == "hundred":
                temp_num *= 100
            elif word in Solution.big_num:
                temp_num *= Solution.big_num[word]
                final_num += temp_num
                temp_num = 0

        final_num += temp_num
        return final_num


sol = Solution()
s = "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
sol.word_to_numb(s=s)
# num=1234567891

s = "Twelve Thousand Three Hundred Forty Five"
sol.word_to_numb(s=s)

s = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
sol.word_to_numb(s=s)

