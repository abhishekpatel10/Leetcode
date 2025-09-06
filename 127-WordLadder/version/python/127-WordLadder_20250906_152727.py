# Last updated: 9/6/2025, 3:27:27 PM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque()
        s = set(wordList)
        q.append((beginWord,1))
        while q:
            curr_word , stops = q.popleft()
            if curr_word == endWord:
                return stops
            for i in range(len(curr_word)):
                for ch in range(97,123):
                    if chr(ch) == curr_word[i]:
                        continue
                    nei = curr_word[:i] + chr(ch) + curr_word[i+1:]
                    if nei in s:
                        q.append((nei,stops + 1))
                        s.remove(nei)
        return 0
        
        