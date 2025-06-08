// Last updated: 6/8/2025, 11:54:25 AM
class Solution {
    public String reverseVowels(String s) {
        HashSet<Character> vowels = new HashSet<>(Arrays.asList('a','e','i','o','u','A', 'E' , 'I' , 'O' , 'U' ));
        char[] str = s.toCharArray();
        int left = 0;
        int right = s.length() - 1;
        while(left < right){
            while(left < right && !vowels.contains(str[left])){
                left++;
            }
            while(left < right && !vowels.contains(str[right])){
                right--;
            }
            char temp = str[left];
            str[left] = str[right];
            str[right] = temp;

            left++;
            right--;


        }

        return new String(str);


        

    }
}