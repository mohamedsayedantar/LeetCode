import numpy as np
class Solution:
    def trap(self, height: List[int]) -> int:
        new_arr = np.array(height)
        start, end, holes = 0, len(height)-1, 0
        while start<end:
            lowest = min(new_arr[start], new_arr[end])
            low_area = np.where(np.logical_and(new_arr[start:end]>=0, new_arr[start:end]<lowest))
            
            for i in low_area[0]:
                holes += lowest - new_arr[i+start]
                new_arr[i+start] = lowest
                    
            if new_arr[start]<new_arr[end]:
                start += 1
            else:
                end -= 1
        return holes
        