# Last updated: 6/8/2025, 11:55:06 AM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res , sol = [] , []


        def dfs(i):
            if i >= len(s):
                res.append(sol[:])
                return
            for j in range(i,len(s)):
                if isParti(s,i,j):
                    sol.append(s[i:j+1])
                    dfs(j+1)
                    sol.pop()
        
        def isParti(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        dfs(0)
        return res
