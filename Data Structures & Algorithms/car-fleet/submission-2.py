class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # monotonic stack problem
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            # calculate time + append to stack
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
