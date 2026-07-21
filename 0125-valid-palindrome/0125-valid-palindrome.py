class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ""
        for i in s:
            asci = ord(i)
            if (97 <= asci and asci <= 122) or (48 <= asci and asci <= 57):
                t += i
            
        
        return t == t[::-1]
