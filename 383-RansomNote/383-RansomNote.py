# Last updated: 6/8/2025, 11:54:21 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = len(ransomNote)
        m = len(magazine)

        if r > m :
            return False
        
        hash_map = {}

        for i in magazine:
            if i in hash_map:
                hash_map[i] +=1
            else:
                hash_map[i] = 1
        
        for i in ransomNote:
            if i not in hash_map:
                return False
            elif hash_map[i] == 1:
                del hash_map[i]
            else:
                hash_map[i] -= 1
        
        return True