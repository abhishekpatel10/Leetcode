# Last updated: 8/10/2025, 4:14:44 PM
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            return tuple(sorted(str(x)))
        
        target = count_digits(n)
        
        for i in range(31): 
            if target == count_digits(1 << i):
                return True
        return False