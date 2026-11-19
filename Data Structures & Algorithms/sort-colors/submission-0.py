class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def heap(nums, n, i):
            largest = i
            l = 2 * i + 1
            r = l + 1

            if l < n and nums[l] > nums[largest]:
                largest = l
            if r < n and nums[r] > nums[largest]:
                largest = r
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heap(nums, n, largest)


        n = len(nums)

        i = n // 2 - 1
        while i >= 0:
            heap(nums, n, i)
            i -= 1
            
        for i in range(n-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heap(nums, i, 0)
	
        """
        Do not return anything, modify nums in-place instead.
        """
        