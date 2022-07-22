class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1  = {}
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]].append(i)
            else:
                dict1[s[i]] = [i]
                
        for i in dict1:
            if len(dict1[i]) == 1:
                return dict1[i][0]
            
        return -1