class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        j = n - 1
        i = 0

        while i != n:
            s = numbers[i] + numbers[j]

            if s == target:
                return [i+1, j+1]
            elif s < target:
                i += 1
            else:
                j -= 1
                
            
            