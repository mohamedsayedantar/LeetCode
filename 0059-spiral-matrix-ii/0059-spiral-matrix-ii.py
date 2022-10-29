class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        z = []
        for i in range(n):
            z.append([0] * n)
        
        state = "right"
        i, j = 0, 0
        for k in range(n*n):
            #print(k,state,i,j)
            if state == "right":
                z[i][j] = k+1
                if j+1 <= n-1:
                    if z[i][j+1] == 0:
                        j += 1
                    else:
                        state = "down"
                        i += 1
                else:
                    state = "down"
                    i += 1
            elif state == "down":
                z[i][j] = k+1
                if i+1 <= n-1:
                    if z[i+1][j] == 0:
                        i += 1
                    else:
                        state = "left"
                        j -= 1
                else:
                    state = "left"
                    j -= 1
                    
            elif state == "left":
                z[i][j] = k+1
                if j-1 >= 0:
                    if z[i][j-1] == 0:
                        j -= 1
                    else:
                        state = "up"
                        i -= 1
                else:
                    state = "up"
                    i -= 1
                    
            else:
                z[i][j] = k+1
                if i-1 >= 0:
                    if z[i-1][j] == 0:
                        i -= 1
                    else:
                        state = "right"
                        j += 1
                else:
                    state = "right"
                    j += 1
                    
            
        #print(z)
        return z
                