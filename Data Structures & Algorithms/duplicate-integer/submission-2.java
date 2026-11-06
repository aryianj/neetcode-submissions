class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> dups = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (dups.get(nums[i]) != null) {
                return true;
            }
            dups.put(nums[i], i);
        }
        return false;
    }
}