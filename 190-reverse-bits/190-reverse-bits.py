class Solution:
    def reverseBits(self, n: int) -> int:
        
        return int((((32 - len(str(bin(n)[2:])))*"0") + str(bin(n)[2:]))[::-1], 2)