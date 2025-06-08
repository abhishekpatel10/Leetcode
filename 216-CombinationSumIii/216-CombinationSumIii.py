# Last updated: 6/8/2025, 11:54:43 AM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res ,sol= [],[]
        curr_sum = 0
        def backtrack(i,curr_sum):
            if len(sol) == k and curr_sum == n:
                res.append(sol[:])
                return
            
            if i >=10 or curr_sum > n:
                return
            sol.append(i)
            backtrack(i+1,curr_sum +i)
            sol.pop()

            backtrack(i+1,curr_sum)

        backtrack(1,0)
        return res