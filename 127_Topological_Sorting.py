__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """

    # Solution 1: BSF
    def topSort(self, graph):

        # Define indegree with dict (not contain 0 indegree node)
        result = []
        indegree = {}
        
        for i in graph:
            for j in i.neighbors:
                if j in indegree:
                    # more than one neighbors
                    indegree[j] += 1
                else: 
                    # one neighbors
                    indegree[j] = 1
        # queue
        q = []
        for node in graph:
            # Not in the indegree, means this node is one of the begin node
            if node not in indegree:
                q.append(node)
                result.append(node)
                
        while len(q) > 0:
            n = q.pop(0)
            for neighbor in n.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    result.append(neighbor)
                    q.append(neighbor)

        return result

    # Solution 2 (not recommend): DFS with extra for loop to init the indegree dict with 0  
    # def topSort(self, graph):   
        #define indegree with dict
        # indegree = dict((i,0) for i in graph)
        # for i in graph:
        #     for j in i.neighbors:
        #         indegree[j]+=1
                
        # #define queue and put the 0 degree nodes

        # q = []
        # for i in graph:
        #     if indegree[i] == 0:
        #         q.append(i)
                
        # #result and bfs       
        # result = []        
        # while len(q) > 0:
        #     node = q.pop(0)
        #     result.append(node)
        #     for j in node.neighbors:
        #         indegree[j]-=1
        #         if indegree[j] == 0:
        #             q.append(j)
                    
        # return result
        
    # Solution 3: DFS
    # def dfs(self, i, countrd, ans):
    #     ans.append(i)
    #     countrd[i] -= 1
    #     for j in i.neighbors:
    #         countrd[j] -= 1
    #         if countrd[j] == 0:
    #             self.dfs(j, countrd, ans)

    # def topSort(self, graph):
    #     # write your code here
    #     countrd = {}
    #     for x in graph:
    #         countrd[x] = 0

    #     for i in graph:
    #         for j in i.neighbors:
    #             countrd[j] += 1

    #     ans = []
    #     for i in graph:
    #         if countrd[i] == 0:
    #             self.dfs(i, countrd, ans)
    #     print(ans)
    #     return ans