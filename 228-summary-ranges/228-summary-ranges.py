class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr = []
        if len(nums) == 0:
            return []
        
        first, second = 0, 0
        for i in range(len(nums)):
            if nums[i] == nums[first]:
                pass
            elif nums[i] == nums[second] +1:
                second = i
            else:
                if first != second:
                    arr.append(str(nums[first]) + "->" + str(nums[second]))
                else:
                    arr.append(str(nums[first]))
                
                first, second = i, i
        
        if first != second:
                arr.append(str(nums[first]) + "->" + str(nums[second]))
        else:
                arr.append(str(nums[first]))
        return arr