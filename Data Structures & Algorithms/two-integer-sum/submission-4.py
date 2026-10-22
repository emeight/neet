class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}   # value: index
        for i, num in enumerate(nums):
            # compute the required complement
            comp = target - num
            if comp in seen.keys():
                return [seen[comp], i]
            seen[num] = i
