// Last updated: 6/8/2025, 11:54:02 AM
class Solution {
    public boolean judgeSquareSum(int c) {
        long smallest = 0;
        long largest = (long) Math.sqrt(c);

        while(smallest<= largest){
            long sum = smallest * smallest + largest * largest;
            if(sum == c){
                return true;
            }
            else if (sum < c){
                smallest++;
            }
            else{
                largest--;
            }
        }

        return false;
        
        
    }
}