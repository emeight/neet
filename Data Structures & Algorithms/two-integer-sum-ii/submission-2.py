class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init pointers at both ends of list
        l = 0
        r = len(numbers) - 1
        # loop until they meet
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            if total < target:
                # need bigger sum, increase left pointer
                l += 1
            else:
                # need smaller sum, decrease right pointer
                r -= 1
        # shouldn't get here
        return []