class Solution:
    def __init__(self, s):
        self.s = s

    def resoult(self):
        opposite = {")": "(", "]": "[", "}": "{"}
        check = []
        for i in s:
            if i not in opposite.keys() or len(check) == 0:
                check.append(i)
            elif opposite[i] == check[-1]:
                check.pop()

        return len(check) == 0


s = "()"
res = Solution(s)
print(res.resoult())
