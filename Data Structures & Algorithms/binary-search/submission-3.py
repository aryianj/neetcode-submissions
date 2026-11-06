class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low: int, high: int, nums: List[int], target: int) -> int:
            if low > high:
                return -1
            
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, high, nums, target)
            return binary_search(low, mid -1, nums, target)

        return binary_search(0, len(nums) - 1, nums, target)
        

