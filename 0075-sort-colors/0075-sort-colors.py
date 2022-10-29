class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one, two = 0, 0, 0
        for i in nums:
            if i==1:
                one +=1
            elif i==0:
                zero += 1
            else:
                two += 1
                
        for i in range(len(nums)):
            if zero > 0:
                nums[i] = 0
                zero -= 1
            elif one > 0:
                nums[i] = 1
                one -= 1
            else:
                nums[i] = 2
                two -= 1
        """
        while one+two+zero > 0:
            if zero > 0:
                nums[pointer] = 0
                zero -= 1
                pointer += 1
            elif one > 0:
                nums[pointer] = 1
                one -= 1
                pointer += 1
            else:
                nums[pointer] = 2
                two -= 1
                pointer += 1
        """