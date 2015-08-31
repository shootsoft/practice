__author__ = 'yinjun'

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        # write your code here

        if node in self.dict:
            return self.dict[node]

        c = UndirectedGraphNode(node.label)
        self.dict[node] = c

        for n in node.neighbors:
            c.neighbors.append(self.cloneGraph(n))

        return c