// Last updated: 6/8/2025, 11:53:14 AM
class Solution {
    public String reverseOnlyLetters(String s) {
        if(s == null || s.isEmpty()){
            return "";
        }
        char[] arr = s.toCharArray();
        int left = 0;
        int right = s.length() - 1;

        while(left < right){
            while(left < right && !Character.isLetter(s.charAt(left))){
                left++;
            }
            while(left < right && !Character.isLetter(s.charAt(right))){
                right--;
            }
            if(left< right){
                char temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;

                left++;
                right--;
            }
        }

        return new String(arr);
        

        
    }
}