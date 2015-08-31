__author__ = 'yinjun'

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here

        if graph == None:
            return []

        return self.topSortBFS(graph)

    def topSortBFS(self, graph):

        result = []

        first = self.findFirst(graph)
        if first == None:
            return result

        queue = list()
        queue += first

        s = set()
        while len(queue)>0:
            p = queue.pop(0)
            result.append(p)
            s.add(p)

            if p !=None and p.neighbors !=None:
                for n in p.neighbors:
                    if p not in s:
                        queue.append(n)

        if len(s) < len(graph):
            result += list(set(graph) - s)
        return result


    def findFirst(self, graph):

        g_set = set(graph)
        for n in graph:
            if n.neighbors!= None:
                for nb in n.neighbors:
                    if nb == n:
                        continue
                    elif nb in g_set:
                        #print nb.label
                        g_set.remove(nb)

        if len(g_set) > 0:
            return list(g_set)
        else:
            return None



# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


n0 = DirectedGraphNode(0)
n1 = DirectedGraphNode(1)
n2 = DirectedGraphNode(2)
n3 = DirectedGraphNode(3)
n4 = DirectedGraphNode(4)

n1.neighbors = [n3, n4]
n2.neighbors = [n1, n4]
n3.neighbors = [n4]

graph = [n4, n3, n2, n1, n0]

s = Solution()

print '[',
for n in s.topSort(graph):
    print n.label,
print ']'




