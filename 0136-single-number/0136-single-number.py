class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = collections.Counter(nums)
        return (min(dict1, key=dict1.get))