class Solution {
    public int majorityElement(int[] nums) {
       HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) != null) {
                Integer count = map.get(nums[i]);
                map.put(nums[i], count+1);
            } else {
                map.put(nums[i], 1);
            }
        } 
        List<Map.Entry<Integer, Integer>> sortedList = map.entrySet().stream().sorted(Map.Entry.comparingByValue()).collect(Collectors.toList());
        
        int[] result = sortedList.stream().mapToInt(Map.Entry::getKey).toArray();
        return result[result.length-1];


        
    }
}