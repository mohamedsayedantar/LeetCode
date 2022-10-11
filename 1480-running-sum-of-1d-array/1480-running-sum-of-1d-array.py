class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        value = 0
        out = []
        for i in range(len(nums)):
            value += nums[i]
            out.append(value)
            
        return out