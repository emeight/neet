class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '{': '}', '[': ']'}
        # walk the string
        for c in s:
            if c in d.keys():
                stack.append(d[c])
            else:
                # if the stack is empty we're beginning with a closure
                if not stack:
                    return False
                b = stack.pop()
                if c != b:
                    return False
        return not stack
        