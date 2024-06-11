class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #  such that i < j < k and nums[i] < nums[j] < nums[k]

        # ngebuat 2 angka pertama itu terkecil
        num_i = num_j = float('inf')
        # num i = num j = tak hingga +

        for num in nums:
            # maksa cari i paling kecil
            if num <= num_i:
                num_i = num
            # kalo dah dapet i terkecil cari terkecil setelah j
            elif num <= num_j:
                num_j = num
            else:
                return True

        return False
