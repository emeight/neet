class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        l = ""
        t = 0
        o = ""
        for s in strs:
            sl = len(s)
            l += f"{sl}_"
            o += s
            t += sl

        return o + l + str(t)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        # index of t
        ti = len(s) - s[::-1].find("_")
        t = int(s[ti:])
        # grab full string
        o = s[:t]
        # grab str lens
        l = s[t:ti-1].split("_")
        strs = []
        c = 0
        for i in l:
            n = int(i)
            strs.append(o[c:c+n])
            c += n
        return strs
