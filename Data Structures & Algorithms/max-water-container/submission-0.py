class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l: int = 0
        r: int = len(heights) - 1
        area: int = 0

        while l < r:
            lH = heights[l]
            rH = heights[r]

            h = min(lH, rH)
            w = r - l
            area = max(area, h * w)

            if lH < rH:
                l += 1
            else:
                r -= 1
        return area