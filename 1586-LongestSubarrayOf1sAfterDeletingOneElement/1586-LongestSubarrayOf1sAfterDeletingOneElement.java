// Last updated: 6/8/2025, 11:52:47 AM
class Solution {
    public int longestSubarray(int[] nums) {
        int max_w = 0;
        int zeroCount = 0;
        int l = 0 ;
        
        for (int r = 0 ; r <nums.length ; r++){
            if(nums[r] == 0){
                zeroCount++;
            }

            while(zeroCount == 2){
                if(nums[l] ==0){
                    zeroCount--;
                }
                l++;
            }
            max_w = Math.max(r - l , max_w);
        }
        return max_w;
    }
}