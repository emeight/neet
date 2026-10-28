class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        n = len(nums)

        # init pointer
        for i in range(n - 2):
            # skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # zero is the smallest possible triplet
            if nums[i] > 0:
                break

            # if -i = j + k, [i, j, k] is a triplet
            target = -nums[i]
            j = i + 1
            k = n - 1

            # two pointers on the space to the right of i
            while j < k:
                cand = nums[j] + nums[k]
                if cand < target:
                    # increase
                    j += 1
                elif cand > target:
                    # decrease
                    k -= 1
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    # tighten
                    j += 1
                    k -= 1
                    # skip duplicate j/k vals
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return out
