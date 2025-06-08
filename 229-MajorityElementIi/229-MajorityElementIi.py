# Last updated: 6/8/2025, 11:54:39 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        el1 = None
        el2 = None
        ans = []
        for i in range(len(nums)):
            if cnt1 == 0 and el2 != nums[i]:
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and el1 != nums[i]:
                cnt2 = 1
                el2 = nums[i]
            elif el1 == nums[i]:
                cnt1 += 1
            elif el2 == nums[i]:
                cnt2 += 1
            else:
                cnt1 -=1
                cnt2 -= 1
        count1 = 0
        count2 = 0
        for num in nums:
            if num == el1:
                count1 +=1
            if num == el2:
                count2+= 1
        if count1>len(nums)//3:
            ans.append(el1)
        if count2>len(nums)//3:
            ans.append(el2)


        return ans