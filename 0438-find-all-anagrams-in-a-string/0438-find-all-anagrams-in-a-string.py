class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0,                   'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0,                   'w':0, 'x':0, 'y':0, 'z':0,}
        
        s_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0,                   'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0,                   'w':0, 'x':0, 'y':0, 'z':0,}
        for char in p :
            p_dict[char] += 1
            
        length = len(p)
        out = []
        
        for i in range(len(s)):
            if i >= length:
                s_dict[s[i]] += 1
                s_dict[s[i-length]] -= 1
            else:
                s_dict[s[i]] += 1
                
            if p_dict == s_dict:
                out.append(i-(length-1))
                
        return out