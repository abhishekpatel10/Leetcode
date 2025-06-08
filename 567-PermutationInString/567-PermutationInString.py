# Last updated: 6/8/2025, 11:54:05 AM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub1 = len(s1)
        sub2 = len(s2)

        if sub1 > sub2:
            return False
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(sub1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1
        
        if s1_counts == s2_counts:
            return True
        
        for i in range(sub1,sub2):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i -sub1]) - 97] -= 1

            if s1_counts == s2_counts:
                return True

        return False

