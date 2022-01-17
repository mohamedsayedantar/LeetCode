class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = len(board)-1
        self.columns = len(board[0])-1
        def find_O(i,j):
            if i>=0 and i<=self.rows and j>=0 and j<=self.columns: 
                if board[i][j]=="O":
                    board[i][j] = "T"
                    find_O(i+1,j)
                    find_O(i-1,j)
                    find_O(i,j+1)
                    find_O(i,j-1)
                    
        for i in range(self.rows+1):
            if board[i][0]=="O":
                find_O(i,0)
                
        for i in range(self.rows+1):
            if board[i][self.columns]=="O":
                find_O(i,self.columns)
        
        for j in range(self.columns+1):
            if board[0][j]=="O":
                find_O(0,j)
        
        for j in range(self.columns+1):
            if board[self.rows][j]=="O":
                find_O(self.rows,j)
                
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if board[i][j]=="O":
                    board[i][j] = "X"
                    
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if board[i][j]=="T":
                    board[i][j] = "O"
        
