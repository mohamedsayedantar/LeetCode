class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer = 0
        for i in nums2:
            while nums1[pointer]<=i and pointer< m:
                pointer +=1
            if pointer < m:
                nums1[pointer+1:m+1] = nums1[pointer:m]
            m += 1
            nums1[pointer] = i
        