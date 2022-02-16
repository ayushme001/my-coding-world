class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word=0
        for i in range(0, len(sentences)):
            count=len(sentences[i].split())
            print(count, " ", max_word)
            if count > max_word:
                max_word=count
                
        return max_word