class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        columns = len(matrix[0])
        first = 0
        end = rows-1
        #last_i = 0
        while first+1 != end and end > first:
            middle = int((first + end) / 2)
            #print(first, end,middle)
            if matrix[middle][0] <= target:
                first = middle
            else:
                end = middle
        
        if target >= matrix[end][0]:
            row = end
        else:
            row = first
            
        first = 0
        end = columns-1
        
        if target ==  matrix[row][first]:
            return True
        if target ==  matrix[row][end]:
            return True
        
        while first+1 != end and end > first:
            middle = int((first + end) / 2)
            #print(first, end,middle)
            if matrix[row][middle] == target:
                return True
            elif target > matrix[row][middle]:
                first = middle
            else:
                end = middle
                
        return False
        
        """
        rows = len(matrix)
        columns = len(matrix[0])
        last_i = 0
        for i in range(rows):
            #print(i)
            if matrix[i][0] <= target:
                last_i = i
            else:
                break
        for i in range(columns):
            #print(last_i, i)
            if matrix[last_i][i] == target:
                return True
        return False
        """