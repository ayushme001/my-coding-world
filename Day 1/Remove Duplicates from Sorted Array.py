class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = list(set(nums))
        a.sort()
        n = len(a)
        nums[:n] = a
        return len(a)