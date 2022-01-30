import math
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        print(xor)
        count = 0
        for _ in range(32):
            count += xor & 1
            xor = xor >> 1
        return count
        
        