class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        L = len(s)
        if L == 0:
            return True
        for t_char in t:
            if pointer == L:
                return True
            s_char = s[pointer]
            
            if t_char == s_char:
                pointer += 1
                
        #print(L, pointer)
        if pointer == L:
            return True
        else:
            return False
            