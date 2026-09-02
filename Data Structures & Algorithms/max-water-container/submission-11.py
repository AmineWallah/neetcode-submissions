class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr, rptr = 0, len(heights) - 1
        max_volume = 0

        while lptr < rptr:
            volume = min(heights[lptr], heights[rptr]) * (rptr - lptr)
            max_volume = max(max_volume, volume)

            if heights[lptr] < heights[rptr]:
                lptr += 1
            else:
                rptr -= 1

        return max_volume