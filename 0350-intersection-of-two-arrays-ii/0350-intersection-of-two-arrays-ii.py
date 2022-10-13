class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output_list = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and nums1[i]>=0:
                    #print(i, j, nums1[i], nums2[j])
                    output_list.append(nums1[i])
                    nums1[i], nums2[j] = -1, -1
        
        return output_list