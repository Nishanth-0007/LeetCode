class Solution:
    def reverse(self, x: int) -> int:
        revx = int(str(abs(x))[::-1])

        if x < 0:
            revx = 0 - revx
        
        left = -2**31
        right = 2**31 - 1

        if revx > right or revx < left:
            revx = 0 


        return revx