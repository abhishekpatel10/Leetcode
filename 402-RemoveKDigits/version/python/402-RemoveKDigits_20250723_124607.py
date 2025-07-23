# Last updated: 7/23/2025, 12:46:07 PM
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []
        for i in range(len(num)):
            while ans and k > 0 and int(ans[-1])  > int(num[i]):
                ans.pop()
                k -=1
            ans.append(num[i])
        while k > 0 and ans:
            ans.pop()
            k -=1
        res = ''.join(ans).lstrip('0')
        
        return res if res else "0"
