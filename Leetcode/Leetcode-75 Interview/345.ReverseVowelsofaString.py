class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # kenalin vowels
        vowels = 'aiueoAIUEO'
        # i, j = 0, len(s) - 1 . memiliki maksud sama kayak dibawah
        i = 0
        j = len(s) - 1
        cs = list(s)
        while i < j:
            if cs[i] not in vowels:
                i += 1
            elif cs[j] not in vowels:
                j -= 1
            else:
                cs[i], cs[j] = cs[j], cs[i]
                i += 1
                j -= 1
        return ''.join(cs)
