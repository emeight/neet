class Solution:
    def trap(self, height: List[int]) -> int:
        # init pointers at each end
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        # iterate until pointers meet
        while left < right:
            # actions if our left pointer is at a height below
            # that of the right pointer
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # water is trapped since we know this all sits
                    # below height[right]
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # water is trapped since we know this all sits
                    # below height[left]
                    water += right_max - height[right]
                right -= 1
        return water
