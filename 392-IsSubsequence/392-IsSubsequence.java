// Last updated: 6/8/2025, 11:54:23 AM
class Solution {
    public boolean isSubsequence(String s, String t) {
        int i=0,j=0;
        int n = s.length();
        int m = t.length();
        while(i<n && j<m){
            if(s.charAt(i) == t.charAt(j)){
                i++;j++;
            }else{
                j++;
            }
        }

        if(i==n) return true;
        return false;
    }
}