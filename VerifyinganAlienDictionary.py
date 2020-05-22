class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dictionary = {}
        for i in range(len(order)):
            dictionary[order[i]] = i

        n = len(words)
        for i in range(1, n):
            word1, word2 = words[i-1], words[i]
            len_w1 = len(word1)
            len_w2 = len(word2)
            short_length = len_w1 if len_w1 < len_w2 else len_w2
            for i in range(short_length):
                if dictionary[word1[i]] > dictionary[word2[i]]:
                    return False
                elif dictionary[word1[i]] == dictionary[word2[i]]:
                    continue
                else:
                    break
            if word1[:short_length] == word2[:short_length] and len_w1 > len_w2:
                return False
        return True
