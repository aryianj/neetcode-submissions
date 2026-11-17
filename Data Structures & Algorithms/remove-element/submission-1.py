class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        i, n = 0, len(nums)-1
        while i < n:
            if nums[i] == val:
                nums.append(nums.pop(i))
                n -= 1
            else:
                i += 1
        return k