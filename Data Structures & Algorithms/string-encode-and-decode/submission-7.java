class Solution {

    public String encode(List<String> strs) {
        String ec = "";

        for (String str : strs) {
            int len = str.length();
            ec = ec.concat(len + "#" + str);
        }
        return ec;
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        String tempStr = "";
        int temp = 0;

        if (str.length() == 2) {
            strs.add("");
            return strs;
        }

        for (int i = 0; i < str.length(); i++) {
            while (Character.isDigit(str.charAt(i)) && str.charAt(i) != '#') {
                tempStr = tempStr.concat(str.charAt(i) + "");
                i++;
            }
             if (!tempStr.isEmpty()) {
                temp = Integer.parseInt(tempStr);
            }

            tempStr = "";
            i += 1; 
            
            strs.add(str.substring(i, i + temp));
            
            i = (i + temp) - 1;
        }
        return strs;
    }
}
