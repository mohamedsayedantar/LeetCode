class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1 = {}
        
        for char in s:
            if char in dict1:
                dict1[char] = dict1[char] + 1
            else:
                dict1[char] = 1
                
        odd = False
        out = 0
        
        for char in dict1:
            i = dict1[char]
            if i % 2 == 0:
                out += i
            elif i > 1:
                out += i-1
                if odd == False:
                    odd = True
                    out += 1
            else:
                if odd == False:
                    odd = True
                    out += 1
                    
        return out