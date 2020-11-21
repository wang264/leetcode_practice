# # 99. Recover Binary Search Tree
# # Hard
#
# # You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
# # Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
#
# Example 1:
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
#
# Example 2:
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
#
# Constraints:
# The number of nodes in the tree is in the range [2, 1000].
# -231 <= Node.val <= 231 - 1


from helperfunc import TreeNode, build_tree_breadth_first


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.first = None
        self.second = None

        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            # special case, the smallest node
            if self.pre is None:
                self.pre = root
            else:
                if self.pre.val > root.val:
                    if self.first is None:
                        self.first = self.pre
                    self.second = root

                self.pre = root

            inorder(root.right)

        inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val


tree = build_tree_breadth_first([3, 1, 4, None, None, 2])
sol = Solution()
sol.recoverTree(root=tree)

