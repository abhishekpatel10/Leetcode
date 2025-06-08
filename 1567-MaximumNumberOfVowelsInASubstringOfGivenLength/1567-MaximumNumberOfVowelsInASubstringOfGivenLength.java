// Last updated: 6/8/2025, 11:52:49 AM
class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        int i = 0 ;
        int j = 0 ;
        int max = Integer.MIN_VALUE;
        int ans = 0;
        while(j < s.length()){
            if(vowels.contains(s.charAt(j))){
                ans++;
            }
            if( j-i + 1 <k){
                j++;
            }
            else if(j - i + 1 ==k){
                max = Math.max(ans , max);
                if(vowels.contains(s.charAt(i))){
                    ans--;
                }
                i++;
                j++;
            }
        }

        return max;
    }
}