class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sliding window
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                # ignore self
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        # should not reach
        return [i, j]
        