class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub : dict = {}

        for i in range(len(nums)):
            temp : int = target - nums[i]

            if temp in sub:
                return [sub[temp], i]
            sub[nums[i]] = i

        return [0,0]

