class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        # init pointers on each end
        i, j = 0, len(heights) - 1
        while i < j:
            # compute area
            area = (j - i) * min(heights[i], heights[j])
            if area > max_area:
                max_area = area
            # move the pointer with the lesser height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
