// Last updated: 6/8/2025, 11:52:56 AM
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ans1 = new ArrayList<>();
        List<Integer> ans2 = new ArrayList<>();
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for(int i : nums1){
            set1.add(i);
        }

        for(int j: nums2){
            set2.add(j);
        }

        for(int i:set1){
            if(!set2.contains(i)){
                ans1.add(i);
            }
        }

        for(int j:set2){
            if(!set1.contains(j)){
                ans2.add(j);
            }
        }

        ans.add(ans1);
        ans.add(ans2);
        return ans;


    }
}