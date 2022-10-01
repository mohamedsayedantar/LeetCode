class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        arr = nums
        def findleft(array, target, left, right):
            middle = floor((left+right) /2)
            #print(left, middle, right)
            if left == middle :
                if array[left] == target:
                    return left
                elif array[right] == target:
                    return right
                else:
                    return -1
            
            if array[left] == target:
                return left
            elif array[middle] >= target:
                return findleft(array, target, left, middle)
            else:
                return findleft(array, target, middle, right)
            
            
        def findright(array, target, left, right):
            middle = ceil((left+right) /2)
            #print(left, middle, right)
            if right == middle :
                if array[right] == target:
                    return right
                elif array[left] == target:
                    return left
                else:
                    return -1
            
            if array[right] == target:
                return right
            elif array[middle] <= target:
                return findright(array, target, middle, right)
            else:
                return findright(array, target, left, middle)
            
            
            
        first = findleft(arr, target, 0, len(arr)-1)
        last = findright(arr, target, 0, len(arr)-1)
        output = []
        
        if first == -1:
            return []
        
        while first <= last:
            output.append(first)  
            first += 1
            
        return output
        
        