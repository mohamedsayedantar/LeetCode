class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        dict1 = {}
        color = image[sr][sc]
        for i in range(m):
            for j in range(n):
                if image[i][j]==color:
                    dict1[str(i)+","+str(j)] = "yes"
                else:
                    dict1[str(i)+","+str(j)] = "no"
                            
        stack = []
        stack.append([sr,sc])
        while len(stack)>0:
            element = stack[-1]
            stack.pop(-1)
            if dict1[str(element[0])+","+str(element[1])]!="true":
                if str(element[0])+","+str(element[1]+1) in dict1:
                    if dict1[str(element[0])+","+str(element[1]+1)]=="yes":
                        stack.append([element[0],element[1]+1])
                    
                if str(element[0])+","+str(element[1]-1) in dict1:
                    if dict1[str(element[0])+","+str(element[1]-1)]=="yes":
                        stack.append([element[0],element[1]-1])
                        
                if str(element[0]+1)+","+str(element[1]) in dict1:
                    if dict1[str(element[0]+1)+","+str(element[1])]=="yes":
                        stack.append([element[0]+1,element[1]])
                        
                if str(element[0]-1)+","+str(element[1]) in dict1:
                    if dict1[str(element[0]-1)+","+str(element[1])]=="yes":
                        stack.append([element[0]-1,element[1]])
                        
                image[element[0]][element[1]] = newColor
                dict1[str(element[0])+","+str(element[1])] = "true"
                
        return image