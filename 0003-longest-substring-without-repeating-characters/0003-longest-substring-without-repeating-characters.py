class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = set()
        maxi = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                maxi = max(maxi, len(seen))       
            else:
                seen.remove(s[l])
                l += 1
        
        return maxi

