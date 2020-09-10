# 987. Vertical Order Traversal of a Binary Tree
# Medium
#
# Share
# Given a binary tree, return the vertical order traversal of its nodes values.
#
# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
#
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
#
# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
#
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
from typing import List

from binary_tree_helper import TreeNode, deserialize


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        min_heap = []
        x = 0
        y = 0
        stack = [(x, y, root)]

        while stack:
            x, y, node = stack.pop()
            # by default python is a minheap, so because we want to iterate y position from large to small, we insert -1*y instead
            # if for two item in the heap, if their coordinate are the same, i should
            heapq.heappush(min_heap, (x, -1 * y, node.val))
            if node.left:
                # heapq.heappush(min_heap, (x - 1, y - 1, node.left.val))
                stack.append((x - 1, y - 1, node.left))
            if node.right:
                # heapq.heappush(min_heap, (x + 1, y - 1, node.right.val))
                stack.append((x + 1, y - 1, node.right))

        print(min_heap)
        rslt = []
        curr_x = min_heap[0][0]
        curr_lvl = []
        while min_heap:
            x, neg_y, val = heapq.heappop(min_heap)

            if x != curr_x:
                rslt.append(curr_lvl)
                curr_lvl = []
                curr_x = x
                curr_lvl.append(val)
            else:
                curr_lvl.append(val)

        rslt.append(curr_lvl)

        return rslt


sol = Solution()
root = deserialize('[3,9,20,null,null,15,7]')
rslt = sol.verticalTraversal(root)

sol_2 = Solution()
root_2 = deserialize('[1,2,3,4,5,6,7]')
rslt = sol_2.verticalTraversal(root_2)

# hua hua jiang
class Solution2:

    def preorder(self, root, x, y, vals):
        if not root:
            return
        vals.append((x, y, root.val))
        # y+1 intead of y-1 here is because for the same x, y need to process descendingly, but the sort function
        # in python sort by ascendingly.
        self.preorder(root.left, x - 1, y + 1,vals)
        self.preorder(root.right, x + 1, y + 1,vals)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        vals = []

        self.preorder(root, 0, 0, vals)
        ans = []
        last_x = -1000
        for x, y, val in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(val)
        return ans