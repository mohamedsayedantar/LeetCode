class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1  = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]].append(i)
            else:
                dict1[nums[i]] = [i]
            
        for i in range(len(nums)):
            remain = target - nums[i]
            
            if remain in dict1:
                list1 = dict1[remain]
                for i2 in list1:
                    if i != i2:
                        return [i, i2]

            
        