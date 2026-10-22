class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [(num,freq)]
        counts = {}
        # single pass
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        # sort, grab top k
        return sorted(counts, key=counts.get, reverse=True)[:k]
