class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for s in strs:
            # sorted() -> sorts string to alphabetic list of chars
            g[''.join(sorted(s))].append(s)
        return list(g.values())
