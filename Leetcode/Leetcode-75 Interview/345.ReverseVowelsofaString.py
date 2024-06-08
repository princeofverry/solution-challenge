class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # kenalin vowels
        vowels = 'aiueoAIUEO'
        i = 0,
        j = len(s) - 1
        cs = list(s)
        while i < j:
