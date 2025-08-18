# Last updated: 8/18/2025, 3:25:31 PM
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps = 1e-6
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) <= eps
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    temp = []
                    for val in range(n):
                        if val != i and val !=j :
                            temp.append(nums[val])
                    a = nums[i]
                    b = nums[j]
                    possible = [(a*b),(a-b),(b-a),(a+b)]
                    if abs(a) > eps:
                        possible.append(b/a)
                    if abs(b) > eps:
                        possible.append(a/b)
                    for pos in possible:
                        temp.append(pos)
                        if solve(temp):
                            return True
                        temp.pop()
            return False
        return solve(cards)
                        
                    

