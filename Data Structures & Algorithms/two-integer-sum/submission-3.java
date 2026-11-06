class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sol = {};
        for (int i = 0; i < nums.length; i++) {
            for (int j = 1; j < nums.length; j++) {
                if (nums[j] + nums[i] == target && i != j) {
                    return new int[]{i, j};
                }
            }
        }
            return sol;

    }
}
