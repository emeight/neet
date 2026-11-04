import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for s in tokens:
            if s not in {"+","-","*","/"}:
                stk.append(int(s))
            else:
                a = stk.pop()
                b = stk.pop()

                if s == "+":
                    stk.append(b+a)
                elif s == "-":
                    stk.append(b-a)
                elif s == "*":
                    stk.append(b*a)
                else:
                    stk.append(math.trunc(b/a))

        return stk[-1]