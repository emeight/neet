class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # sorted letters : []
        for s in strs:
            l = []
            for c in s:
                l.append(ord(c))
            # key
            k = str(sorted(l))
            if k not in groups.keys():
                groups[k] = [s]
            else:
                groups[k].append(s)

        return [groups[p] for p in groups.keys()]
