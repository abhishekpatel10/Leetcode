# Last updated: 7/31/2025, 1:06:34 PM
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        memo = set()

        def dfs(i, curr_or):
            if i == len(arr):
                return
            key = (i, curr_or)
            if key in memo:
                return  # skip repeated work
            memo.add(key)

            curr_or |= arr[i]
            result.add(curr_or)
            dfs(i + 1, curr_or)

        for i in range(len(arr)):
            dfs(i, 0)

        return len(result)
        