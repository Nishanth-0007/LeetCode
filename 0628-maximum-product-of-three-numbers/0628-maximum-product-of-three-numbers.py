class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        l1 = nums[n-3:]
        l2 = nums[:2]
        l2.append(nums[n-1])
        i = 0

        return max(math.prod(l2), math.prod(l1))