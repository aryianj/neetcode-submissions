class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, area = 0, 0
        r: int = len(heights) - 1

        while l < r:
            lH: int = heights[l]
            rH: int = heights[r]

            h = min(lH, rH)
            w = r - l

            area = max(area, h * w)

            if lH < rH:
                l += 1
            else:
                r -= 1
        return area