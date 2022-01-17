class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1 = {}
        check = {}
        
        list_s = s.split()
        p_len = len(pattern)
        s_len = len(list_s)
        
        if p_len != s_len:
            return False
        
        for i in range(p_len):
            if pattern[i] in dict1:
                if dict1[pattern[i]] != list_s[i]:
                    return False
            else:
                if list_s[i] in check:
                    return False
                dict1[pattern[i]] = list_s[i]
                check[list_s[i]] = 1
            
        return True