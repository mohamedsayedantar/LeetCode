class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        self.state = True
        def find_island(i, j):
            if i>=0 and i<rows and j>=0 and j<columns:
                if grid[i][j]==0:
                    grid[i][j] = "T"
                    if i==0 or i==(rows-1) or j==0 or j==(columns-1):
                        self.state = False
                    find_island(i+1, j)
                    find_island(i-1, j)
                    find_island(i, j+1)
                    find_island(i, j-1)
            
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==0:
                    self.state = True
                    find_island(i, j)
                    if self.state:
                        islands += 1
                        
        return islands
                    
            