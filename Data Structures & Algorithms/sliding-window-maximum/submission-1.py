class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sums = []
        for i in range(len(nums) - k + 1):
            maxElm = float('-inf')
            for j in range(k):
                maxElm = max(maxElm, nums[i + j])
            sums.append(maxElm)

        return sums
