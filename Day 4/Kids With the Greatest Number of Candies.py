class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        list=[]
        max_candies=max(candies)
        for i in range(0, len(candies)):
            if candies[i]+extraCandies >= max_candies:
                list.append(True)
            else:
                list.append(False)
                
        return list