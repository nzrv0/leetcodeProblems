class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        target = self.target
        nums = self.nums
        
        resoult = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    resoult = [i, j]

        return resoult


nums = [3, 2, 3]
target = 6
res = Solution(nums, target)
print(res.twoSum())
