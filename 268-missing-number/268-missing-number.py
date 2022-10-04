class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        L = len(nums)
        myset = set()
        for i in range(L+1):
            myset.add(i)
            
        for num in nums:
            myset.remove(num)
        
        for num in myset:
            return num