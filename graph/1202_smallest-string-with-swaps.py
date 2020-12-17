# 1202. Smallest String With Swaps
# Medium
#
# You are given a string s, and an array of pairs of indices in the string pairs where
# pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
# You can swap the characters at any pair of indices in the given pairs any number of times.
#
# Return the lexicographically smallest string that s can be changed to after using the swaps.
#
# Example 1:
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
#
# Example 2:
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
#
# Example 3:
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
#
# Constraints:
# * 1 <= s.length <= 10^5
# * 0 <= pairs.length <= 10^5
# * 0 <= pairs[i][0], pairs[i][1] < s.length
# * s only contains lower case English letters.

from typing import List


class Solution:
    # use DFS to find the connect component of pairs,
    # the smallest subsequence of each component is achived by sort the char in the connected component.
    # then we iterate all connected component and try to update the final string.
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph_node_to_neighbors = dict()
        for i in range(len(s)):
            graph_node_to_neighbors[i] = set()

        for node_a, node_b in pairs:
            graph_node_to_neighbors[node_a].add(node_b)
            graph_node_to_neighbors[node_b].add(node_a)

        component_id_to_value = dict()
        component_id_to_index = dict()
        visited_index = set()
        curr_component_id = 0
        for idx_a, _ in pairs:
            if idx_a in visited_index:
                continue
            else:
                self.dfs_visit_pairs(s, curr_component_id, idx_a, visited_index, component_id_to_value,
                                     component_id_to_index, graph_node_to_neighbors)
                curr_component_id += 1

        s_as_list = list(s)
        for component_id in component_id_to_index.keys():
            sorted_index = sorted(component_id_to_index[component_id])
            sorted_value = sorted(component_id_to_value[component_id])
            for i, idx in enumerate(sorted_index):
                s_as_list[idx] = sorted_value[i]
        new_s = ''.join(s_as_list)
        return new_s

    def dfs_visit_pairs(self, s, component_id, start_index, visited, component_id_to_value, component_id_to_index,
                        graph_node_to_neighbors):
        if start_index in visited:
            return
        visited.add(start_index)
        if component_id not in component_id_to_index:
            component_id_to_index[component_id] = list()
        component_id_to_index[component_id].append(start_index)

        if component_id not in component_id_to_value:
            component_id_to_value[component_id] = list()
        component_id_to_value[component_id].append(s[start_index])

        for neighbor in graph_node_to_neighbors[start_index]:
            self.dfs_visit_pairs(s, component_id, neighbor, visited, component_id_to_value, component_id_to_index,
                                 graph_node_to_neighbors)


# sol = Solution()
# sol.smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]])

sol = Solution()
sol.smallestStringWithSwaps(s="pwqlmqm",pairs=[[5,3],[3,0],[5,1],[1,1],[1,5],[3,0],[0,2]])