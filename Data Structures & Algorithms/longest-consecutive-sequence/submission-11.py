class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        nums = sorted(list(set(nums)))
        res, streak, i = 0, 0, 0
        curr = nums[0]

        while i < len(nums):
            if curr != nums[i]:
                streak = 0
                curr = nums[i]
            i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res

