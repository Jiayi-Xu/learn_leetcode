class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for s in str:
            if ord(s) < 91 and ord(s) > 64 :
                res.append(chr(ord(s) + 32))
            else:
                res.append(s)

        return ''.join(res)