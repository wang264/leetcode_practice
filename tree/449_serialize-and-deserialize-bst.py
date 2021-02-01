# 449. Serialize and Deserialize BST
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
# in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
# another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
# serialized to a string and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
# Note: Do not use class member/global/static variables to store states. Your serialize
# and deserialize algorithms should be stateless.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
from collections import deque

from binary_tree_helper import TreeNode, deserialize


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        rslt = []
        self._serialize_pre_order(root, rslt)
        return ' '.join(rslt)

    def _serialize_pre_order(self, root, rslt):
        if not root:
            return
        rslt.append(str(root.val))
        self._serialize_pre_order(root.left, rslt)
        self._serialize_pre_order(root.right, rslt)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None

        data_stream = deque(data.split(" "))
        return self._deserialize(data_stream, -sys.maxsize, sys.maxsize)

    # cur_min: the minimum allowed number for the next node.
    # curr_max: the maximum allowed number for the next node.
    def _deserialize(self, data_stream, cur_min, cur_max):
        if not data_stream:
            return None
        # this value is not part of the subtree
        val = int(data_stream[0])
        if val < cur_min or val > cur_max:
            return None
        data_stream.popleft()
        tree_node = TreeNode(val)
        tree_node.left = self._deserialize(data_stream, cur_min, val)
        tree_node.right = self._deserialize(data_stream, val, cur_max)
        return tree_node


# Your Codec object will be instantiated and called as such:

codec = Codec()
root = deserialize('[2,1,3]')
data = codec.serialize(root)
root_rslt = codec.deserialize(data)


root_2 = None
data_2 = codec.serialize(root_2)
root_rslt_2 = codec.deserialize(data_2)

# codec.deserialize(codec.serialize(root))
