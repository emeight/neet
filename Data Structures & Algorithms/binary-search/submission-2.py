class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] < target:
                # throw out left side
                low = mid + 1
            elif nums[mid] > target:
                # throw out right side
                high = mid - 1
            else:
                # found it
                return mid

        # not found
        return -1
