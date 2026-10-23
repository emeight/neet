class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix + suffix
        l = len(nums)
        p = [1] * l

        # we want to compiute everything to the left and right of the index
        # left pass -> product of everything to the left of i
        left = 1
        for i in range(l):
            p[i] = left
            left *= nums[i]

        # right pass -> product of everything to the right of i
        right = 1
        for i in range(l - 1, -1, -1):
            p[i] *= right
            right *= nums[i]

        return p