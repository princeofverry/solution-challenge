class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l = len(candies)
        ans = []  # return list true / false of kids with candies
        for i in range(l):
            if candies[i]+extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
