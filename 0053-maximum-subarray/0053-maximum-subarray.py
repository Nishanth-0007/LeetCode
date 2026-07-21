class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = 0
        maxi = nums[0]
        

        for i in range(len(nums)):
            curr += nums[i]
            if nums[i] > curr:
                curr = nums[i]
            maxi = max(curr, maxi)

        return maxi
            

        
        
        
        '''n = len(nums)
        maxi = nums[0]
        if n == 1:
            return nums[0]
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum += nums[j]
                maxi = max(sum, maxi)
        
        return maxi'''
