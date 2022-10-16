class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for columns chech
        dict1 = {}
        for row in board:
            for i in row:
                if i == ".":
                    pass
                else:
                    if i in dict1:
                        return False
                    else:
                        dict1[i] = -1
            dict1.clear()
        
        dict1.clear()
        
        for column in range(9):
            for row in board:
                if row[column] == ".":
                    pass
                else:
                    if row[column] in dict1:
                        return False
                    else:
                        dict1[row[column]] = -1
            dict1.clear()
        
        
        
        x=[[0,3,0,3],[0,3,3,6],[0,3,6,9],[3,6,0,3],[3,6,3,6],[3,6,6,9],[6,9,0,3],[6,9,3,6],[6,9,6,9]]
        
        def get(r1,c1,r2,c2):
            dict1.clear()
            for row in board[r1:c1]:
                for elem in row[r2:c2]:
                    if elem == ".":
                        pass
                    else:
                        if elem in dict1:
                            return False
                        else:
                            dict1[elem] = -1
            return True
                        
        for i in x:
            if not get(i[0],i[1],i[2],i[3]):
                return False
                        
        return True
                
        
        