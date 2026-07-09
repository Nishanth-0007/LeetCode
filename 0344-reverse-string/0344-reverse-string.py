class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s1 = s.copy()
        s.clear()
        for i in range(len(s1)-1, -1, -1):
            s.append(s1[i])