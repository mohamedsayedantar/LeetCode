class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)-1
        self.columns = len(grid[0])-1
        self.count = 0
        def find_island(i,j):
            if i>=0 and i<=self.rows and j>=0 and j<=self.columns:
                if grid[i][j] == "1":
                    grid[i][j] = "T"
                    find_island(i+1,j)
                    find_island(i-1,j)
                    find_island(i,j+1)
                    find_island(i,j-1)
            
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if grid[i][j]=="1":
                    find_island(i, j)
                    self.count += 1
                    
        return self.count