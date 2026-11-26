class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dups =  []
        i, n = 0, len(nums) - 1
        while i <= n:
            while i <= n and nums[i] in dups:
                nums.pop(i)
                n -= 1
            if i <= n and nums[i] not in dups:
                dups.append(nums[i])
            i += 1
        return len(nums)
            
            
