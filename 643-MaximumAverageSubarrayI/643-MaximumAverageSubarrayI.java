// Last updated: 6/8/2025, 11:54:03 AM
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double max = Double.NEGATIVE_INFINITY;
        double w_sum = 0;
        int n = nums.length;
        int start = 0;

        for(int i = 0 ; i < n ; i++){
            w_sum += nums[i];

            if(i - start + 1 == k){
                double avg = w_sum/k;
                max = Math.max(max , avg);
                w_sum -= nums[start];
                start++;
            }
        }

        return max;
    }
}