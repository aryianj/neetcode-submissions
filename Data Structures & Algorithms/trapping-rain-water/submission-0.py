class Solution:
    def trap(self, height: List[int]) -> int:
        l, res = 0, 0
        r: int = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax =  max(rightMax, height[r])
                res += rightMax - height[r]

        return res