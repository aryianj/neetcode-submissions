class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub : dict = {} # nums[i], index
        # nums = [3, 4, 5, 6], target = 7
        # dict {[7-3=4, 0], [7-4=3, 1], [7-5=2, 2], [7-6=1, 3]= }
        for i in range(len(nums)):
            temp : int = target - nums[i]
            if temp in sub:
                return [sub[temp], i]
            sub[nums[i]] = i
        
        return [0,0]

