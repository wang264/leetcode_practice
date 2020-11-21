# 450. Delete Node in a BST
# Medium
#
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Follow up: Can you solve it with time complexity O(height of tree)?
#
# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
#
# Example 2:
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
#
# Example 3:
#
# Input: root = [], key = 0
# Output: []
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105

from helperfunc import TreeNode, build_tree_breadth_first


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            new_root = None
            if root.left is None:
                new_root = root.right
            elif root.right is None:
                new_root = root.left
            else:
                # find the min node in the right sub tree
                new_root_parent = root
                new_root = root.right

                while new_root.left:
                    new_root_parent = new_root
                    new_root = new_root.left

                # this is true if the new_root is the right child of the node you want to delete.
                if new_root_parent != root:
                    new_root_parent.left = new_root.right
                    new_root.right = root.right
                new_root.left = root.left

            return new_root

        return root


sol = Solution()
tree = build_tree_breadth_first(sequence=[5, 3, 6, 2, 4, None, 7, 1, 2.5, 3.5, 4.5])

new_tree = sol.deleteNode(root=tree, key=3)

tree = build_tree_breadth_first(sequence=[5, 3, 6, 2, 4, None, 7, 1, 2.5, 3.5, 4.5])

new_tree = sol.deleteNode(root=tree, key=4)
