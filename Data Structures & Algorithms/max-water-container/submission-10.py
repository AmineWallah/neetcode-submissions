class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr = 0
        rptr = len(heights) - 1

        max_volume = 0

        while lptr != rptr:
            volume = 0
            if heights[lptr] > heights[rptr]:
                volume = heights[rptr] * (rptr - lptr)
            else:
                volume = heights[lptr] * (rptr - lptr)
            
            if volume > max_volume:
                max_volume = volume
            
            if heights[lptr] < heights[rptr]:
                lptr += 1
            else:
                rptr -= 1

        return max_volume