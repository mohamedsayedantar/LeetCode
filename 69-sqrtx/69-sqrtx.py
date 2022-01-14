class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        def calc(x, st, end):
            if st+1 == end:
                if end**2==x:
                    return end
                else:
                    return st
            mid = (st+end)//2
            if mid**2<x:
                return calc(x, mid, end)
            else:
                return calc(x, st, mid)
            
        return calc(x, 0, x)
            