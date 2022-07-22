class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if r*c != m*n:
            return mat
        new_mat = [[]]
        counter = 0
        for row in mat:
            for element in row:
                if len(new_mat[counter]) == c:
                    new_mat.append([element])
                    counter += 1
                else:
                    new_mat[counter].append(element)
        return new_mat