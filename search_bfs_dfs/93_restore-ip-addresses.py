# 93. Restore IP Addresses
# Medium
#
# Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can
# return them in any order.
#
# A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots
# and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses
# and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]

# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]

# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

# Constraints:
# 0 <= s.length <= 3000
# s consists of digits only.

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        rslt = []
        curr_path = []
        curr_idx = 0
        self.dfs(s, curr_idx, curr_path, rslt)
        return rslt

    def dfs(self, s, curr_idx, curr_path, rslt):
        if len(curr_path) > 4:
            return

        if len(curr_path) == 4 and curr_idx == len(s):
            rslt.append('.'.join(curr_path))
            return

        for num_digit in [1, 2, 3]:
            if curr_idx + num_digit > len(s):
                continue
            curr_str = s[curr_idx:curr_idx + num_digit]
            # leading zero not allow
            if len(curr_str) > 1 and curr_str[0] == '0':
                continue

            if not (0 <= int(curr_str) <= 255):
                continue

            curr_path.append(curr_str)
            self.dfs(s,curr_idx+num_digit,curr_path, rslt)
            curr_path.pop()

sol =Solution()
sol.restoreIpAddresses(s="101023")