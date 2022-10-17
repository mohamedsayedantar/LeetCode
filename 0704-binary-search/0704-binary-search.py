class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 0:
            return -1
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        
        def get_num(left, right):
            mid = floor((left+right) /2)
            if nums[mid] == target:
                return mid
            
            if right == left + 1 or left==right:
                return -1
            else:
                if nums[mid] > target:
                    return get_num(left, mid)
                else:
                    return get_num(mid, right)
                    
        
        
        return get_num(left, right)