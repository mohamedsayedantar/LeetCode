class Solution:
    def decodeString(self, s: str) -> str:
        
        def get_str(string):
            first_part = ""
            mid_part = ""
            Last_part = ""
            L = len(string)
            count = 0
            count = 0
            var = 0
            brackets = 0
            num = ""
            while count < L:
                if string[count].isdigit() :
                    num += string[count]
                    if string[count+1].isdigit():
                        count += 1
                        num += string[count]
                        if string[count+1].isdigit():
                            count += 1
                            num += string[count]
                    var = int(num)
                    count += 2
                    brackets = 1
                    while brackets != 0:
                        if string[count] == "[":
                            brackets += 1
                            mid_part += string[count]
                            
                        elif string[count] == "]":
                            brackets -= 1
                            if brackets != 0:
                                mid_part += string[count]
                        else:
                            mid_part += string[count]
                            
                        count += 1
                    
                    while count < L:
                        Last_part += string[count]
                        count += 1
                    #print("first: ", first_part, "  second: ", mid_part,"  third: ", Last_part)    
                    return first_part + var * get_str(mid_part) + get_str(Last_part)
                    
                else:
                    first_part += string[count]
                    count += 1
                    
            return string
                    
        return get_str(s)
                    
                    
# r d f g 3 [ s s ] r r         L = 11
# 0 1 2 3 4 5 6 7 8 9 10

# first_part = rdfg