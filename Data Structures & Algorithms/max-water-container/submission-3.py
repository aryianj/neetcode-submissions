class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, area = 0, 0
        r = len(heights) - 1

        while l < r:
            l_h, r_h = heights[l], heights[r]
            w, h = r - l, min(l_h, r_h)
            area = max(area, w * h)
            if l_h < r_h:
                l += 1
            else:
                r -= 1
        return area
