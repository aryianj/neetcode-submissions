class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products : List[int] = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i is not j:
                    products[i] *= nums[j]
        return products