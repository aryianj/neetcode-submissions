class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, area = 0, 0
        r = len(heights) - 1

        while l < r:
            lHeight, rHeight = heights[l], heights[r]
            height = min(lHeight, rHeight)
            width = r - l
            area = max(area, height * width)
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1
        return area