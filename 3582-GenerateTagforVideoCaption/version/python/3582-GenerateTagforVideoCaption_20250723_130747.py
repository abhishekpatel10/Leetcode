# Last updated: 7/23/2025, 1:07:47 PM
class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.lower().split()
        if caption==[]:
            return "#"
        res = list()
        res.append('#')
        res.append(caption[0])
        for i,word in enumerate(caption):
            if i==0:
                pass
            else:
                res.append(caption[i][0].upper()+caption[i][1:])
        caption =  ''.join(res)
        return caption[:100]

