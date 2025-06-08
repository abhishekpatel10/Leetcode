// Last updated: 6/8/2025, 11:54:26 AM
class Solution {
    public void reverseString(char[] s) {
        int left = 0 ;
        int len = s.length;
        int right = len - 1;
        

        while(left < right){
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;

            left++;
            right--;
        
        }

       

    }
}