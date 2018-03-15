__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"
# Referece: http://blog.leanote.com/post/westcode/%5B%E5%88%B7%E9%A2%98%E7%AC%94%E8%AE%B0%5D-LeetCode-LintCode-10

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        
        # # Note for python tips
        # list = []          ## Start as the empty list
        # list.append('a')   ## Use append() to add elements
        # list.append('b')
        # # This insert will only be place at index 2 after 'b'
        # list.insert(100, 'hello')
        # print(list)
        # print(list[2])
        
        result = []
        # indegree = [0 for i in range(numCourses)]
        indegree = [0] * numCourses
        # Graph can not init by indegree's way.
        graph = [[] for i in range(numCourses)]
        
        # count and update indegree
        for pre in prerequisites:
            thenLearnThis = pre[0]
            indegree[thenLearnThis] += 1

            # Add neighbors for each course
            mustLearnFirst = pre[1]
            graph[mustLearnFirst].append(thenLearnThis)
        
        # find the start point
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # bfs to find the topo order
        visited = 0
        while len(q) > 0:
            course = q.pop(0)
            result.insert(visited, course)
            visited += 1
            
            neighbors = graph[course]
            for neighbor in neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                
        if visited == numCourses:
            return result
            
        return []