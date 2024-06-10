# medium
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
         misal si Arr dibalik
         "gg gaming!" output : "gaming! gg"
         
         lalu selanjutnya tambahkan di array baru
         append memasukkan berarti kedalam array

         terus join gabungin kata-kata dalam array l
         jadi satu string dengan spasi pemisah
        """

        Arr = s.split()[::-1]
        l = []
        for i in Arr:
            l.append(i)
        return ' '.join(l)
