class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        L = len(nums)
        dict1 = {}
        for i in range(L+1):
            dict1[i] = "F"
            
        for num in nums:
            dict1[num] = "T"
        
        for num in dict1:
            if dict1[num] == "F":
                return num