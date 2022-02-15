class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums)):
            ans.insert(i,nums[nums[i]])
        return ans
            