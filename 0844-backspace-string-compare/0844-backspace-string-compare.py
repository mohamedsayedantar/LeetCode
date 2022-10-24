class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_text(word):
            output = ""
            counter = 0
            word = word[::-1]
            for i in word:
                if i == '#':
                    counter += 1
                else:
                    if counter > 0:
                        counter -= 1
                    else:
                        output += i
            return output[::-1]
        
        if get_text(s) == get_text(t):
            return True
        else:
            return False