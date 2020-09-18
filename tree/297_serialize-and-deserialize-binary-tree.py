# 297. Serialize and Deserialize Binary Tree
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
# the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
# serialized to a string and this string can be deserialized to the original tree structure.
#
# Example:
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"
#
# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily
# need to follow this format, so please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize
# algorithms should be stateless.
#

from binary_tree_helper import TreeNode
from collections import deque
from binary_tree_helper import deserialize as deserialize_from_helper

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'
        queue = deque([root])
        rslt = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    rslt.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    rslt.append('#')
        return ' '.join(rslt)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_queue = deque(data.split(' '))
        if data_queue[0] == '#':
            return None

        root = TreeNode(int(data_queue.popleft()))
        node_queue = deque([root])
        is_left = True
        while node_queue:
            curr_data = data_queue.popleft()
            if curr_data == '#':
                pass
            else:
                node = TreeNode(int(curr_data))
                node_queue.append(node)
                if is_left:
                    node_queue[0].left = node
                else:
                    node_queue[0].right = node
            if not is_left:
                node_queue.popleft()

            is_left = not is_left
        return root



class CodecRecursive:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        rslt = []
        self._serialize(root, rslt)
        return ' '.join(rslt)

    def _serialize(self, root, rslt):
        if not root:
            rslt.append("#")
            return
        rslt.append(str(root.val))
        self._serialize(root.left,rslt)
        self._serialize(root.right,rslt)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_stream = deque(data.split(" "))
        return self._deserialize(data_stream)

    def _deserialize(self, data_steam: deque):
        char = data_steam.popleft()
        if char == '#':
            return None
        tree_node = TreeNode(int(char))
        tree_node.left = self._deserialize(data_steam)
        tree_node.right = self._deserialize(data_steam)
        return tree_node

# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.deserialize(codec.serialize(root))


codec = Codec()
root = deserialize_from_helper('[1,2,3,null,null,4,5]')

data = codec.serialize(root=root)
root_rslt = codec.deserialize(data)


codec_rec = CodecRecursive()
data_rec = codec_rec.serialize(root)
root_rslt_rec = codec_rec.deserialize(data=data_rec)