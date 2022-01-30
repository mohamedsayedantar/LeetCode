import math
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        X = str(bin(x)[2:])
        Y = str(bin(y)[2:])
        X_len = len(X)
        Y_len = len(Y)
        
        if X_len>Y_len:
            Y = str(0)*(X_len-Y_len) + Y
        else:
            X = str(0)*(Y_len-X_len) + X
        
        out = 0
        for i in range(len(X)):
            if X[i] != Y[i]:
                out += 1
                
        return out
        