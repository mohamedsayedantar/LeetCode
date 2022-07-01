class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            count = len(sentence.split())
            if max_words < count:
                max_words = count
            #print(max_words)
        return max_words