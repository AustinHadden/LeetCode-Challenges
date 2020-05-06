class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = set()

        for i in nums:

            if i not in dic:
                dic.add(i)
            else:
                return i

        return False