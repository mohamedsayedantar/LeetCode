class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for x in nums:
            if x in dict1:
                return True
            else:
                dict1[x] = 1
        
        return False