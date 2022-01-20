class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        dict1 = {}
        b = b % len(s)
        
        def find(word, a, b):
            if word not in dict1:
                dict1[word] = 1
                d = list(word)
                
                for i in range(len(d)):
                    if i%2 != 0:
                        d[i] = str((int(d[i])+a) %10)
                
                find("".join(d), a, b)
                
                for i in range(b):
                    word = word[-1] + word[:-1]
                
                find(word, a, b)
                
        
        find(s, a, b)
        return min(dict1)