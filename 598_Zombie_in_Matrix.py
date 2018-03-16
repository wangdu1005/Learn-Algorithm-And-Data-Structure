class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    PEOPLE = 0
    ZOMBIE = 1
    WALL = 2
    
    def zombie(self, grid):

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
            
        n, m = len(grid), len(grid[0])
        print(grid)

        cpGrid = []
        for col in grid:
            cpGrid.append(col)
        print(cpGrid)
        
        q = []
        people_left = 0
        days = 0
        
        for i in range(n):
            for j in range(m):
                if cpGrid[i][j] == self.PEOPLE:
                    people_left += 1
                elif cpGrid[i][j] == self.ZOMBIE:
                    q.append((i, j))

        if people_left == 0:
            return 0
        
        # BFS
        while len(q) > 0:
            days += 1
            size = len(q)
            for i in range(size):
                p = q.pop(0)

                for dx, dy in dirs:
                    bitex = p[0] + dx
                    bitey = p[1] + dy

                    # check if out of boundary
                    if bitex < 0 or bitex >= n or bitey < 0 or bitey >= m:
                        continue
                    
                    # check if bitetable
                    if cpGrid[bitex][bitey] is not self.PEOPLE:
                        continue

                    people_left -= 1
                    cpGrid[bitex][bitey] = self.ZOMBIE
                    q.append((bitex, bitey))
            if people_left == 0:
                return days
        return -1