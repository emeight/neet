class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [(num,freq)]
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        return sorted(counts, key=counts.get, reverse=True)[:k]
