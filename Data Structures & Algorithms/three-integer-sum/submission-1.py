class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0 
                    and i != j 
                    and j != k 
                    and i != k 
                    and sorted([nums[i], nums[j], nums[k]]) not in res):
                        res.append(sorted([nums[i], nums[j], nums[k]]))
        return res
