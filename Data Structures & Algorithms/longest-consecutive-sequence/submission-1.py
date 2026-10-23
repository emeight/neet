class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0
        s = set(nums)
        # find starters
        for n in s:
            if n-1 not in s:
                o = [n]
                m = n + 1
                while m in s:
                    o.append(m)
                    m += 1
                if len(o) > l:
                    l = len(o)

        return l
        