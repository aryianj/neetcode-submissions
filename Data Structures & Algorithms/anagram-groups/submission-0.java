class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> res = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            int[] base = new int[26];

            for (int j = 0; j < strs[i].length(); j++) {
                base[strs[i].charAt(j) - 'a']+= 1;
            } 
            String key = Arrays.toString(base);
            res.computeIfAbsent(key, k -> new ArrayList<>()).add(strs[i]);
        } 
        return new ArrayList(res.values());
    }

}
