class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            y = target - num
            if y in h:
                return [h[y], i]
            else:
                h[num] = i