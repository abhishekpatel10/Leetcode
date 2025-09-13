# Last updated: 9/13/2025, 12:42:22 PM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        con = 0
        vow = 0
        d_set = set(s)
        print(d_set)
        for i in d_set:
            if i in 'aeiou':
                vow = max(vow,s.count(i))
                print(s.count(i))
            else:
                con = max(con,s.count(i))
                print('.>>>>',s.count(i))
        return vow + con