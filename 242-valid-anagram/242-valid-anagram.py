class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return collections.Counter(s) == collections.Counter(t)
        dict1 = {}
        dict2 = {}
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
                
        for i in t:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
                
        if dict1 == dict2:
            return True
        else:
            return False
        