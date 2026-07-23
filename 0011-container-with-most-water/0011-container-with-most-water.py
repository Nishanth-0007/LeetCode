class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        area = 0
        while right != left:
            
            
            area = max(area, min(height[right], height[left]) * (right - left))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        
        return area




