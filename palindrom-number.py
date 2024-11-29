class Solution:
    def __init__(self, x):
        self.x = x

    def twoSum(self):
        
        x = str(self.x)
        if x == x[::-1]:
            return True

        return False


x = 121
res = Solution(x)
print(res.twoSum())
