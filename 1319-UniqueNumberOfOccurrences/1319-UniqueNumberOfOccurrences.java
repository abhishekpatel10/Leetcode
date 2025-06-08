// Last updated: 6/8/2025, 11:52:57 AM
class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int i : arr){
            hm.put(i, hm.getOrDefault(i,0)+1);
        }

        HashSet<Integer> hs = new HashSet<>();

        for(int i : hm.values()){
            if(!hs.add(i))
            return false;
        }
        return true;
        
    }
}