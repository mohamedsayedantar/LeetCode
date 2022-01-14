class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def calc(x, st, end):
            if st+1 == end:
                if end**2==x:
                    return True
                elif st**2==x:
                    return True
                else:
                    return False
            mid = (st+end)//2
            if mid**2<x:
                return calc(x, mid, end)
            else:
                return calc(x, st, mid)
            
        return calc(num, 0, num)