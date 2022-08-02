class Solution:
    def isValid(self, s: str) -> bool:
        
        my_list = []
        for i in s:
            if i == "(":
                my_list.append(i)
            elif i == ")":
                if len(my_list)>0:
                    if my_list[-1] == "(":
                        my_list.pop(-1)
                    else:
                        return False
                else:
                    return False
            elif i == "{":
                my_list.append(i)
            elif i == "}":
                if len(my_list)>0:
                    if my_list[-1] == "{":
                        my_list.pop(-1)
                    else:
                        return False
                else:
                    return False
            elif i == "[":
                my_list.append(i)
            elif i == "]":
                if len(my_list)>0:
                    if my_list[-1] == "[":
                        my_list.pop(-1)
                    else:
                        return False
                else:
                    return False
            else:
                return False
            #print(my_list)
            
        
        if len(my_list)>0:
                return False
        else:
            return True
        