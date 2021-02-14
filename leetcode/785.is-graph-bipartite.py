#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) == 1:
            if graph[0] == []:
                return True
            return False
        colors = [-1 for _ in range(len(graph))]
        # -1: not colored; 0: color a; 1: color b
        for i in range(len(graph)):
            if colors[i] == -1 and not self.valid(graph, colors, i, 0):
                return False
        return True
    
    # if colors[index] is not colored, color it, and check its next indices' conficts
    # if it is colored, check if it is equal to color
    def valid(self, graph, colors, index, color):
        # check conflicts
        if colors[index] != -1:
            return color == colors[index]
        # not yet colored
        colors[index] = color
        # check its next indices
        for i in graph[index]:
            if not self.valid(graph, colors, i, 1-color):
                return False
        return True


        
# @lc code=end

