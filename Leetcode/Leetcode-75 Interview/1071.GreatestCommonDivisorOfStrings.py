class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # periksa apakah salah satu string digabungkan dengan string lainnya
        # meriksa apakah urutan berpengaruh
        if str1 + str2 != str2 + str1:
            return ''

        def gcd(a, b):
            # selama b bukan 0 dia akan terus lanjut
            while b:
                # a = b, dan b akan = a % b
                a, b = b, a % b
            return a

        # mengembalikan str1 dari pembagian gcd
        # dengan indeks pembagian gcd a
        return str1[:gcd(len(str1), len(str2))]
