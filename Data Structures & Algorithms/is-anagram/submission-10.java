class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> sMap = new HashMap<String, Integer>();
        HashMap<String, Integer> tMap = new HashMap<String, Integer>();

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {

            int sCount = sMap.containsKey(s.charAt(i) + "") ? sMap.get(s.charAt(i) + "") : 0;
            int tCount = tMap.containsKey(t.charAt(i) + "") ? tMap.get(t.charAt(i) + "") : 0;

            sMap.put(s.charAt(i) + "", sCount + 1);
            tMap.put(t.charAt(i) + "", tCount + 1);
        }

        for (String i : sMap.keySet()) {
            Integer sInt = sMap.get(i);
            Integer tInt = tMap.get(i);
            
            if (!sInt.equals(tInt)) {
                return false;
           }
        }
        return true;
    }
}
