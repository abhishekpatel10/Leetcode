// Last updated: 6/8/2025, 11:54:38 AM
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] arr = new int[nums.length];
        for(int i = 0 ; i <nums.length ; i++){
            arr[i] = 1;
        }
        int left = 1;
        for(int i =0 ; i <nums.length ; i++){
            arr[i] *= left;
            left *= nums[i];
        }

        int right = 1 ;
        for(int i =nums.length - 1 ; i  >=0 ; i--){
            arr[i] *= right;
            right *= nums[i];
        }
        return arr;
    }
}