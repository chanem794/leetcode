class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i in range(len(words)):
            # words[i] = words[i].reverse()
            words[i] = words[i][::-1]
        res = " ".join(words)
        return res
        
        