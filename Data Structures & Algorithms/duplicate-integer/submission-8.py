class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2: set = set(nums)

        return len(nums) != len(nums2)