class Solution:
    def isPalindrome(self, x: int) -> bool:
        revx = str(x)[::-1]

        if revx == str(x):
            return True

        return False
