class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            val = 2 ** i
            if n == val:
                return True
            elif n < val:
                return False
        
        return False
