class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        
        for i in range(len(nums)):
            if i == 0:
                right -= nums[0]
                left = 0
            else:
                right -= nums[i]
                left += nums[i-1]
                
            if right == left :
                return i
            
        return -1