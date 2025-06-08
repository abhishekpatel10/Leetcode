# Last updated: 6/8/2025, 11:55:13 AM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def pascalTriangle(n):
            res = 1
            ansrow = [1]
            for i in range(1,n):
                res = res*(n-i)
                res = res // i
                ansrow.append(res)
            return ansrow
        ans =[]
        for i in range(1,numRows+1):
            ans.append(pascalTriangle(i))
        return ans