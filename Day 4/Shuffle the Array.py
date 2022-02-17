class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        print(len(nums)-n)
        list=[]
        for i in range(0, len(nums)-n):
            list.append(nums[i])
            list.append(nums[i+n])
            
        return list