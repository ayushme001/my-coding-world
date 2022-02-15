class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        newList = []
        largestValue = 0
        for i in range(0, len(accounts)):
            if largestValue < sum(accounts[i]):
                largestValue = sum(accounts[i])
        return largestValue