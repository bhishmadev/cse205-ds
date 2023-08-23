class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        jword1="".join(word1)
        jword2="".join(word2)

        if jword1==jword2:
            return True
        else:
            return False