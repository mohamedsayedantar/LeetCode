class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1  = {}
        for i in range(len(magazine)):
            if magazine[i] in dict1:
                dict1[magazine[i]].append(i)
            else:
                dict1[magazine[i]] = [i]
                
        for char in ransomNote:
            if char in dict1:
                if len(dict1[char]) >1:
                    dict1[char].pop(-1)
                else:
                    dict1.pop(char)
            else:
                return False
        return True