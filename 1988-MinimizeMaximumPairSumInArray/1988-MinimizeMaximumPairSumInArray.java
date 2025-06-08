// Last updated: 6/8/2025, 11:52:33 AM
class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int maxSum = 0;
        int pairs = nums.length/2;

        for(int i = 0 ; i < pairs ; i++){
            int pairSum = nums[i] + nums[nums.length - i - 1];

            maxSum = Math.max(maxSum , pairSum); 
        }

        return maxSum;
    }
}