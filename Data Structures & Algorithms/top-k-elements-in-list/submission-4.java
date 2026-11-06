class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        
        List<Map.Entry<Integer, Integer>> sorted = map.entrySet().stream().sorted((e1, e2) -> e2.getValue().compareTo(e1.getValue())).collect(Collectors.toList());

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < k && i < sorted.size(); i++) {
            result.add(sorted.get(i).getKey());
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
        
    }
}
