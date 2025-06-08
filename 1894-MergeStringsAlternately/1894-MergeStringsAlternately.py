# Last updated: 6/8/2025, 11:52:35 AM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A , B = len(word1) , len(word2)
        word = 1
        ans = []
        a , b = 0 , 0

        while a <A and b < B:
            if word == 1:
                ans.append(word1[a])
                a+=1
                word = 2
            elif word == 2:
                ans.append(word2[b])
                b+=1
                word = 1
        
        while a < A:
            ans.append(word1[a])
            a += 1
        while b < B:
            ans.append(word2[b])
            b+= 1

        return ''.join(ans)




        