class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = collections.Counter(nums)
        return (max(dict1, key=dict1.get))