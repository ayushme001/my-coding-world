class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in range(0, len(operations)):
            if "++X" == operations[i] or "X++" == operations[i]:
                x=x+1
            if "--X" == operations[i] or "X--" == operations[i]:
                x=x-1
        return x