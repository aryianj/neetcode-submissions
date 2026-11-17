class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        c = sortedNums[len(nums) // 2]

        if sortedNums.count(c) > len(nums) // 2:
            return c
        return 0
