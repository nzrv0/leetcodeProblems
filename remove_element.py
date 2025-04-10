class Solution:
    def removeElement(self, nums, val):
        resoult = len(list(filter(lambda x: x != val, nums)))
        return resoult


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
solution = Solution()
resoult = solution.removeElement(nums, val)
print(resoult)
getattr()