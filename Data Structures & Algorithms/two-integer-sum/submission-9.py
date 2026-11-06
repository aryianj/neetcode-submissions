class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        # so obviously you can do two four loops.
        # but a for loop is o(n) at most, so it 
        # would be o(n^2) which is bad for runtime
        # and performance.
        # so, you want to use a hashmap to store
        # all previous entries. hashmap lookups are
        # o(1) so it would be o(n) ;)
        # map = {target-nums[i]: i}

        for i in range(len(nums)):
            num = nums[i]
            if num not in map.keys():
                map[target - num] = i
            else:
                return [map[num], i]
        return [-1, -1]
             

        