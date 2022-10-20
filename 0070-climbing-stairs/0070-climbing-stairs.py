class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
            
    
    # 1  2  3  4  5  6  7  8  9  10
    # 1  2  3  5  8  13 21 34