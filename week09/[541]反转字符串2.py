class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        for i in range(0, len(s), 2*k):
            tmp = s[i:i+k]
            s[i:i+k] = tmp[::-1]
        return "".join(s)




class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        res = []
        i = 1
        while i * 2 * k <= len(s):
            tmp = s[(i-1)*k*2:i*k*2-k]
            res.extend(tmp[::-1])
            res.extend(s[i*k*2-k:i*k*2])
            i += 1

        if len(s) - (i-1) * 2 * k < k :
            tmp = s[(i-1) * 2 * k:]
            res.extend(tmp[::-1])
        else:
            tmp = s[(i-1)*k*2:i*k*2-k]
            res.extend(tmp[::-1])
            res.extend(s[i*k*2-k:])
        # print(res)
        return "".join(res)
# i=1 0-4       i*k*2
# i=2 4-8    i*k*2 - k*2 , i*k*2-k ,  i*k*2