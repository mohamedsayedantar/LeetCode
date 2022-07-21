class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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