# Last updated: 9/11/2025, 11:54:16 AM
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        # Step 1: collect vowels from the string
        collected = [ch for ch in s if ch in vowels]
        
        # Step 2: sort the collected vowels
        collected.sort()
        
        # Step 3: rebuild the string, replacing vowels in order
        result = []
        j = 0  # pointer for collected vowels
        for ch in s:
            if ch in vowels:
                result.append(collected[j])
                j += 1
            else:
                result.append(ch)
        
        return "".join(result)

