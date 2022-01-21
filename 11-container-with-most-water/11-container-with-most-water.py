class Solution:
    def maxArea(self, height: List[int]) -> int:
        def get_area(x,y,i,j):
            return min(x,y)* abs(i-j)
        length = len(height)
        areas = []
        start, end = 0, length-1
        while start<end:
            area = get_area(height[start],height[end],start,end)
            areas.append(area)
            
            if height[start]<height[end]:
                start += 1
            else:
                end -= 1
            
        return max(areas)