class Solution:
    def reverseWords(self, s: str) -> str:
        lst =  s.strip().split()
        res = []

        for word in lst:
            res.append(word[::-1])
        return ' '.join(res)