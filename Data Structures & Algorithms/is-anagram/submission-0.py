class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # quick exits
        sl = len(s)
        tl = len(t)
        if sl != tl:
            return False
        ss = set(s)
        ts = set(t)
        if ss != ts:
            return False
        
        def char_freq(x: str, c: str) -> int:
            ctr = 0
            for char in x:
                if char == c:
                    ctr += 1 
            return ctr
        
        for c in ss:
            if char_freq(s, c) != char_freq(t, c):
                return False
        
        return True
            