class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1 = {}
        
        for char in s:
            if char in dict1:
                dict1[char] = dict1[char] + 1
            else:
                dict1[char] = 1
             
        #print(dict1)
        for char in t:
            if char in dict1:
                if dict1[char] > 0:
                    dict1[char] = dict1[char] - 1
                else:
                    #print(dict1)
                    return char
            else:
                #print(dict1)
                return char
            
        