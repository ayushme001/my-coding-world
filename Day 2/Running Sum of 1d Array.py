class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sum_value = 0
        for i in range(0, len(nums)):
            sum_value = sum_value + nums[i]
            sums.insert(i,sum_value)
        return sums
            