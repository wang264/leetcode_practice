# 236. Lowest Common Ancestor of a Binary Tree
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p
# and q as the lowest node in T that has both p and q as descendants (where we allow
# a node to be a descendant of itself).”
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


from binary_tree_helper import TreeNode, deserialize


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, _, lca_node = self.lca_helper(root, p, q)
        return lca_node

    def lca_helper(self, root, p, q):
        # print(root)
        # return (p_in_tree, q_in_tree, lca_node)
        if root is None:
            return False, False, None

        p_in_left, q_in_left, lca_left = self.lca_helper(root.left, p, q)
        p_in_right, q_in_right, lca_right = self.lca_helper(root.right, p, q)

        # one node each side, root must be lca
        if (p_in_left and q_in_right) or (q_in_left and p_in_right):
            return True, True, root
        if (p_in_left and root.val == q.val) or (p_in_right and root.val == q.val):
            return True, True, root
        if (q_in_left and root.val == p.val) or (q_in_right and root.val == p.val):
            return True, True, root

        p_in_tree = p_in_left or p_in_right or root.val == p.val
        q_in_tree = q_in_left or q_in_right or root.val == q.val

        if lca_left:
            return p_in_tree, q_in_tree, lca_left
        if lca_right:
            return p_in_tree, q_in_tree, lca_right

        else:
            return p_in_tree, q_in_tree, None

class Solution2:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # write your code here
        a_in_tree, b_in_tree, lca = self.helper(root, p, q)
        if a_in_tree and b_in_tree:
            return lca
        else:
            return None

    def helper(self, root, node_a, node_b) -> tuple:
        """
        :param root:
        :param node_a:
        :param node_b:
        :return: return tuple of three ( is_a_in_tree, is_b_in_tree, the_lca_node)
        """
        if root is None:
            return False, False, None

        # -----Divide-----#
        a_in_left_tree, b_in_left_tree, lca_left_tree = self.helper(root.left, node_a, node_b)
        a_in_right_tree, b_in_right_tree, lca_right_tree = self.helper(root.right, node_a, node_b)

        # -----Conqure------#
        a_exist_in_tree = a_in_left_tree or a_in_right_tree or root is node_a
        b_exist_in_tree = b_in_left_tree or b_in_right_tree or root is node_b

        if a_exist_in_tree and b_exist_in_tree:
            if lca_left_tree and lca_right_tree:
                pass
            elif lca_left_tree and not lca_right_tree:
                return True, True, lca_left_tree
            elif not lca_left_tree and lca_right_tree:
                return True, True, lca_right_tree
            else:
                # if there are no lca in either subtree the lca must be root
                return True, True, root
        else:
            # if either of A or B does not exist in this tree. it means no LCA, so we return None for LCA.
            return a_exist_in_tree, b_exist_in_tree, None


sol = Solution()
root = deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
sol.lowestCommonAncestor(root, p=TreeNode(5), q=TreeNode(1))

sol = Solution()
root = deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
sol.lowestCommonAncestor(root, p=TreeNode(5), q=TreeNode(4))
