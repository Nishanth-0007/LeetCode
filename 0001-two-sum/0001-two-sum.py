class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        op = []
        for i in range(len(nums)):
            left = target - nums[i]
            if left in seen.keys():
                op.append(i)
                op.append(seen.get(left))

            else:
                seen[nums[i]] = i

        return sorted(op)


        
        