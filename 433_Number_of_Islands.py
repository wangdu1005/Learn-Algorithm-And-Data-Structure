class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # Special condition check
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        
        # Create a mark matrix for record visit information
        visit = [[False for i in range(n)]for j in range(m)]
        print(visit)
        
        # Define an inner function "check", which is for checking the bounds
        # and the coordinate (coor) is visited before or not.
        def check(x, y):
            if x >= 0 and x<m and y>= 0 and y< n and grid[x][y] and visit[x][y] == False:
                return True
                
        # Define an inner BFS function, using queue to explore those un-visit coor
        def bfs(x,y):
            # This is an right, up, left, down coordinate two array, 
            # it is for checking the nearby (nb) island of current visit coor  
            nbrow = [1,0,-1,0]
            nbcol = [0,1,0,-1]
            
            # queue
            q=[(x,y)]
            while len(q) > 0:
                x = q[0][0]
                y = q[0][1]
                q.pop(0)
                for k in range(4):
                    newx = x + nbrow[k]
                    newy = y + nbcol[k]
                    if check(newx, newy):
                        visit[newx][newy] = True
                        q.append((newx,newy))
        
        # Go to every coordinate and check it the visit status first, 
        # then use BFS check the current coor's neighbors 
        count = 0
        for row in range(m):
            for col in range(n):
                if check(row,col):
                    visit[row][col] = True
                    bfs(row,col)
                    count+=1
        return count