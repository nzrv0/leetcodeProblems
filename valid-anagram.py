class Solution:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def resoult(self):
        s = [i for i in self.s]
        x = [i for i in self.t]
        s.sort()
        x.sort()
        print(s, x)
        return True if x == s else False


s = "anagram"
t = "nagaram"
res = Solution(s, t)
print(res.resoult())
