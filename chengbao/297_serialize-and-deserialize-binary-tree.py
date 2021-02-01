# 297. Serialize and Deserialize Binary Tree
# Hard

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
#

from helperfunc import TreeNode, build_tree_breadth_first

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        rslt = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    rslt.append("#")
                    continue
                rslt.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ' '.join(rslt)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_q = deque(data.split(" "))
        # special case, root is None
        if data_q[0] == "#":
            return None
        root = TreeNode(int(data_q.popleft()))
        node_q = deque([root])
        is_left = True

        while node_q:
            node_data = data_q.popleft()
            if node_data == "#":
                pass
            else:
                node = TreeNode(node_data)
                if is_left:
                    node_q[0].left = node
                else:
                    node_q[0].right = node
                node_q.append(node)

            if not is_left:
                node_q.popleft()
            is_left = not is_left
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

sol = Codec()

root = build_tree_breadth_first(sequence=[1, 2, 3, None, None, 4, 5])

tree_as_string = sol.serialize(root=root)


root_a = sol.deserialize(data=tree_as_string)
