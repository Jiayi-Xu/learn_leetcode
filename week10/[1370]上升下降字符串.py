class Solution:
    def sortString(self, s: str) -> str:
        # 建立26个字母数组进行计数
        num = [0] * 26
        for ch in s:
            num[ord(ch) - ord('a')] += 1

        res = ''
        count = len(s)

        while count:
            for i in range(26):
                if num[i] > 0:
                    res += chr(i+ord('a'))
                    num[i] -= 1
                    count -= 1
            for i in range(25,-1,-1):
                if num[i] > 0:
                    res += chr(i+ord('a'))
                    num[i] -= 1
                    count -= 1

        return res



# def sortString(self, s: str) -> str:
#         cnt, ans, asc = collections.Counter(s), [], True
#         while cnt:                                                                  # if Counter not empty.
#             for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):   # traverse keys in ascending/descending order.
#                 ans.append(c)                                                       # append the key.
#                 cnt[c] -= 1                                                         # decrease the count.
#                 if cnt[c] == 0:                                                     # if the count reaches to 0.
#                     del cnt[c]                                                      # remove the key from the Counter.
#             asc = not asc                                                           # change the direction, same as asc ^= True.
#         return ''.join(ans)
# https://leetcode.com/problems/increasing-decreasing-string/discuss/531811/JavaPython-3-Two-clean-codes-w-explanation-and-analysis.