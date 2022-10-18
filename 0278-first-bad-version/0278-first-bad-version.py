# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if isBadVersion(left):
            return left
        def get_bad(left,right):
            mid = ceil((left+right)/2)
            if right == left+1 :
                return right
            if isBadVersion(mid):
                right = mid
                return get_bad(left,right)
            else:
                left = mid
                return get_bad(left,right)
                
        return  get_bad(left,right)
        