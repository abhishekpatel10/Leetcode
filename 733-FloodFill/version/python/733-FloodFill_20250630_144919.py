# Last updated: 6/30/2025, 2:49:19 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        og_color = image[sr][sc]
        if og_color == color:
            return image
        image[sr][sc] = color
        q = deque()
        q.append((sr,sc))
        while q:
            for _ in range(len(q)):
                r , c = q.popleft()
                dirs = [(0,1),(1,0),(-1,0), (0,-1)]
                for dr , dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0<= nc < m and image[nr][nc] == og_color:
                        image[nr][nc] = color
                        q.append((nr,nc))
        return image