class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        comps = {}   # complement: index
        for i, n in enumerate(numbers):
            if n in comps.keys():
                return [comps[n]+1, i+1]
            c = target - n
            comps[c] = i
        # should not get here
        return [comps[n]+1, i+1]
