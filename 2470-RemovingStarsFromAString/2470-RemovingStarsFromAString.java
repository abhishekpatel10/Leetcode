// Last updated: 6/8/2025, 11:52:22 AM
class Solution {
    public String removeStars(String s) {
        Stack<Character> str = new Stack<>();
        

        for(int i = 0 ; i < s.length() ;i++){
            if(s.charAt(i) == '*'){
                str.pop();
            }
            else{
                str.push(s.charAt(i));
            }  
        }
        String ans="";
            for(char e:str){
                ans+=e;
            }
        return ans;
     }
}