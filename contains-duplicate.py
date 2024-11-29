class Solution:
    def __init__(self, s):
        self.s = s

    def resoult(self):
        resoult = True if len(set(s)) != len(s) else False
        return resoult


s = [1, 2, 3, 1]
res = Solution(s)
print(res.resoult())
