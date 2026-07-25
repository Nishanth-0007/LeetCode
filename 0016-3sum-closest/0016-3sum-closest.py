class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        close = nums[0] + nums[1] + nums[2]
        n = len(nums)
        
        for i in range(n - 2):

            l = i + 1
            r = n - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:

                s = nums[i] + nums[l] + nums[r]

                if s == target:
                    return target
                elif abs(target - s) <= abs(target - close):
                    close = s
                
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    

        return close