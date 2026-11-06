class Solution {
    public int[] productExceptSelf(int[] nums) {
        // go through each number, multiply them and store that number.
        // go through each number, add the divided number to the array

        // doesnt work for negatives

        // i can think of how to do it without division in o(n^2) time... 
        // two for loops, outside loop for the number you're ignoring
        int[] products = new int[nums.length];
        Arrays.fill(products, 1);

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i != j) {
                    products[i] *= nums[j];
                }
            }
        }
        return products;
    }
}  
