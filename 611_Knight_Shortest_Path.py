__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"
# Referece: https://www.youtube.com/watch?v=muGEbutp7ig

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
            
        m, n = len(grid), len(grid[0])
        
        visited = [[False for i in range(n)] for j in range(m)]

        dirs = [
            ( 1, 2),
            ( 1,-2),
            (-1, 2),
            (-1,-2),
            ( 2, 1),
            ( 2,-1),
            (-2, 1),
            (-2,-1),
        ]
        
        def check(x, y):
            if x >= 0 and x < m and y >= 0 and y < n \
            and not grid[x][y] and not visited[x][y]:
                return True
        
        q = [source]
        steps = 0
        
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                p = q.pop(0)
                if p.x == destination.x and p.y == destination.y:
                    return steps
                    
                for dx, dy in dirs:
                    nx = p.x + dx
                    ny = p.y + dy
                    if check(nx, ny):
                        np = Point(nx, ny)
                        q.append(np)
                        visited[nx][ny] == True
            steps += 1
        
        return -1