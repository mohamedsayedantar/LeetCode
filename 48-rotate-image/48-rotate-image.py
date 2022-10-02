class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)-1
        def rot(K):
            for i in range(n-(2*K)):
                x = 0
                x = matrix[K][i+K]
                matrix[i+K][n-K], x = x, matrix[i+K][n-K]
                matrix[n-K][n-K-i], x = x, matrix[n-K][n-K-i]
                matrix[n-K-i][K], x = x, matrix[n-K-i][K]
                matrix[K][i+K] = x
            
        
        repeat = ceil(len(matrix) / 2)
        for i in range(repeat):
            rot(i)
        #print(repeat)
            
            
            
            
            
            
            
            
"""       
K          
[K,i+K]  [i+k,n-K]  [n-k,n-K-i]  [n-K-i,K]




"""     