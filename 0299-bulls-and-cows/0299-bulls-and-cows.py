class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        sec_dict = {}
        guess_dict = {}
        x = 0
        y = 0
        
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                x += 1
            else:
                if secret[i] in sec_dict:
                    sec_dict[secret[i]] += 1
                else:
                    sec_dict[secret[i]] = 1
                    
                if guess[i] in guess_dict:
                    guess_dict[guess[i]] += 1
                else:
                    guess_dict[guess[i]] = 1
                
                
        for i in sec_dict:
            if i in guess_dict:
                if sec_dict[i] <= guess_dict[i]:
                    y += sec_dict[i]
                else:
                    y += guess_dict[i]
                    
        return str(x)+"A"+str(y)+"B"        
        
        
        
        