class Solution:
    def searchInsert1(self, nums: List[int], target: int) -> int:
        ans=len(nums)-1
        if max(nums) < target:
            return len(nums)
        if min(nums) > target:
            return 0
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            if(nums[i]>target and nums[i]<nums[ans]):
                ans = i
        return ans

    def searchInsert2(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.insert(0,target)
            nums.sort()
            return nums.index(target)
                