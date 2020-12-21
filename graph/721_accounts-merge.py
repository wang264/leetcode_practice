# 721. Accounts Merge
# Medium
#
# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
#
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
#
# Example 1:
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Note:
#
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].


from typing import List


class Solution:
    def __init__(self):
        self.father = dict()
        self.owner = dict()
        self.root_node_to_its_sons = dict()

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # init
        self.father = dict()
        self.owner = dict()
        self.root_node_to_its_sons = dict()

        # we use union-find algo for each email.

        # we first initialize the emails.
        for account in accounts:
            name, *emails = account
            for email in emails:
                self.owner[email] = name
                self.father[email] = email

        # for the email in each account we connect them together.
        # the first email will be the father of all other emails
        for account in accounts:
            name, *emails = account
            for i in range(1, len(emails)):
                self.union(emails[i], emails[0])

        for account in accounts:
            name, *emails = account
            for email in emails:
                root_for_this_email = self.find(email)
                if root_for_this_email not in self.root_node_to_its_sons.keys():
                    self.root_node_to_its_sons[root_for_this_email] = list()
                self.root_node_to_its_sons[root_for_this_email].append(email)

        rslt = []
        # iterate through dict root_node_to_its_sons so we can generate the result,
        for root_node, sons_of_root_node in self.root_node_to_its_sons.items():
            account_name = self.owner[root_node]
            emails = sorted(set(sons_of_root_node))
            rslt.append([account_name] + emails)

        return rslt

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_b] = root_a

    def find(self, x):
        # if node is root
        if self.father[x] == x:
            return x

        # find the root
        root = x
        while self.father[root] != root:
            root = self.father[root]

        # perform path compression
        while self.father[x] != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return root

sol = Solution()
sol.accountsMerge(accounts=[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
