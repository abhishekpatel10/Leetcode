# Last updated: 9/6/2025, 12:38:38 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        q = deque()
        n = len(image)
        m = len(image[0])
        temp = image[sr][sc]
        q.append((sr,sc))
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                dirs = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr , dc in dirs:
                    nr = r+ dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == temp:
                        image[nr][nc] = color
                        q.append((nr,nc))
        image[sr][sc] = color
        return image