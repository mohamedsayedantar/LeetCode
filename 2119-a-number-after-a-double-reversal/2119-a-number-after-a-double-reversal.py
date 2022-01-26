class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def rev(n):
            return int(str(n)[::-1])
        
        R2 = rev(rev(num))
        return num==R2 