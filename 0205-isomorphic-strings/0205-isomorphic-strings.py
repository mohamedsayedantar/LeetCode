class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
                #print(dict1)
            else:
                #print(s[i]," is exist as ", t[i])
                if dict1[s[i]] == t[i]:
                    pass
                else:
                    return False
        
        #print("-------------------------------------------- part 2")
        
        for i in range(len(s)):
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
                #print(dict2)
            else:
                #print(t[i]," is exist as ", s[i])
                if dict2[t[i]] == s[i]:
                    pass
                else:
                    return False
                
        return True