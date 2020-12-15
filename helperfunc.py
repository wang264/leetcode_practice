# Graph Node
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return 'val:{} next:{}'.format(self.val, self.next.val if self.next else None)


def build_linked_list_from_array(vals):
    nodes = [ListNode(val) for val in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        left = None if self.left is None else self.left.val
        right = None if self.right is None else self.right.val
        return '(D:{}, L:{}, R:{})'.format(self.val, left, right)


def build_tree_breadth_first(sequence):
    # Create a list of trees
    forest = [TreeNode(x) if x is not None else None for x in sequence]

    # Fix up the left- and right links
    count = len(forest)
    for index, tree in enumerate(forest):
        left_index = 2 * index + 1
        if left_index < count:
            tree.left = forest[left_index]

        right_index = 2 * index + 2
        if right_index < count:
            tree.right = forest[right_index]

    for index, tree in enumerate(forest):
        print('[{}]: {}'.format(index, tree))
    return forest[0]  # root
