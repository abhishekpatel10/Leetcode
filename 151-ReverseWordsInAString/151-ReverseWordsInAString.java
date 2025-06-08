// Last updated: 6/8/2025, 11:54:56 AM
class Solution {
    public String reverseWords(String s) {
       String arr[] = s.split("\\s+");
       StringBuilder sb = new StringBuilder();

       for(int i = arr.length - 1 ; i>=0 ; i--){
        sb.append(arr[i]);
        if( i !=0){
            sb.append(" ");
        }
       }

       return sb.toString().trim();

        
    }
}