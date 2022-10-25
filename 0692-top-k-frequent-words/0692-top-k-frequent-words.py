class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
       
            
        dict1 = {}
        for word in words:
            if word in dict1:
                dict1[word] += 1
            else:
                dict1[word] = 1
        length = 0        
        first_list = [[]]
        out_list = []
        
        old_count = -1
        for i in reversed(dict(sorted(dict1.items(), key=lambda item: item[1]))):
            if old_count == -1:
                old_count = dict1[i]
            if dict1[i] == old_count:
                first_list[-1].append(i)
                old_count = dict1[i]
            else:
                first_list.append([i])
                old_count = dict1[i]
            
                
        for Lst in first_list:
            Lst.sort()
        for Lst in first_list:
            for i in Lst:
                out_list.append(i)
                length += 1
                if length == k:
                    #print (first_list, dict1)
                    return out_list # this out without alphapitical order so it is wrong don't submit
            
        